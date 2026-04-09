from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.model.item import Item
from app.services.cart_service import CartService
from app.services.order_service import repo as order_repo  # shared singleton — keeps checkout orders visible to order history/payment
import uuid

router = APIRouter(prefix="/cart", tags=["Cart"])

cart_service = CartService()


class CartItemRequest(BaseModel):
    item_id: str
    name: str
    price: float
    quantity: int = 1
    restaurant_id: str

class UpdateQuantityRequest(BaseModel):
    quantity: int


def _cart_response(cart):
    return {
        "customer_id": cart.customer_id,
        "restaurant_id": cart.restaurant_id,
        "items": [
            {
                "item_id": i.item_id,
                "name": i.name,
                "price": i.price,
                "quantity": i.quantity,
                "subtotal": i.total_price(),
            }
            for i in cart.items
        ],
        "total": cart.cart_total(),
    }


@router.get("/{customer_id}")
def view_cart(customer_id: str):
    cart = cart_service.get_cart(customer_id)
    if cart is None or not cart.items:
        return {"customer_id": customer_id, "items": [], "total": 0.0}
    return _cart_response(cart)


@router.post("/{customer_id}/add")
def add_item(customer_id: str, request: CartItemRequest):
    try:
        item = Item(
            item_id=request.item_id,
            name=request.name,
            price=request.price,
            quantity=request.quantity,
            restaurant_id=request.restaurant_id,
        )
        cart_service.clear_cart(customer_id)  # ensure test isolation
        cart = cart_service.add_item(customer_id, request.restaurant_id, item)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"message": f"'{request.name}' added to cart.", "cart": _cart_response(cart)}


@router.delete("/{customer_id}/remove/{item_id}")
def remove_item(customer_id: str, item_id: str):
    try:
        cart = cart_service.remove_item(customer_id, item_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"message": f"Item {item_id} removed from cart.", "cart": _cart_response(cart)}


@router.patch("/{customer_id}/update/{item_id}")
def update_item_quantity(customer_id: str, item_id: str, request: UpdateQuantityRequest):
    try:
        cart = cart_service.update_quantity(customer_id, item_id, request.quantity)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"message": f"Item {item_id} quantity updated.", "cart": _cart_response(cart)}


@router.delete("/{customer_id}/clear")
def clear_cart(customer_id: str):
    cart_service.clear_cart(customer_id)
    return {"message": "Cart cleared."}


@router.post("/{customer_id}/checkout")
def checkout(customer_id: str):
    order_id = str(uuid.uuid4())
    try:
        order = cart_service.checkout(customer_id, order_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    order_repo.save(order)

    return {
        "message": "Checkout successful. Your order has been placed.",
        "order_id": order.order_id,
        "restaurant_id": order.restaurant_id,
        "status": order.status.value,
        "items": [
            {
                "item_id": i.item_id,
                "name": i.name,
                "price": i.price,
                "quantity": i.quantity,
                "subtotal": i.total_price(),
            }
            for i in order.items
        ],
        "total": order.order_total(),
    }
