from fastapi import APIRouter, HTTPException
from app.model.item import Item
from app.model.order import Order
from app.model.order_status import OrderStatus
from app.services.delivery_service import DeliveryService
from app.services.order_service import OrderService

router = APIRouter(prefix="/ordering", tags=["Ordering"])
delivery_service = DeliveryService()
order_service = OrderService()

# This route will add an item to an order
@router.post("/{order_id}/add_item")
def add_item(order_id: str, item: Item):
    order = order_service.get_order(order_id)

    if order is None:
        raise HTTPException(status_code = 404, detail = "Order not found")
    
    try:
        order.add_item(item)
    except ValueError as e:
        raise HTTPException(status_code = 400, detail = str(e))
    
    return {"message": f"Item {item.name} added to order {order_id}"}

# This route will remove an item from an order
@router.delete("/{order_id}/remove_item")
def remove_item(order_id: str, item_id: str):
    order = order_service.get_order(order_id)

    if order is None:
        raise HTTPException(status_code = 404, detail = "Order not found")
    
    try:
        order.remove_item(item_id)
    except ValueError as e:
        raise HTTPException(status_code = 400, detail = str(e))
    
    return {"message": f"Item {item_id} removed from order {order_id}"}
    
# this route will get an item from an order
@router.get("/{order_id}/items/{item_id}")
def get_item(order_id: str, item_id: str):
    order = order_service.get_order(order_id)

    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    
    item = order.get_item(item_id)

    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return {
        "item_id": item.item_id,
        "item_name": item.name,
        "item_price": item.price,
        "item_quantity": item.quantity,
        "item_restaurant_id": item.restaurant_id
    }

# This router starts an order
@router.post("/{order_id}/start")
def start_order(order_id: str):
    order = order_service.get_order(order_id)

    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")

    try:
        order.start_order()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    return {"message": f"Order {order_id} has started successfully"}

# This router cancels an order
@router.post("/{order_id}/cancel")
def cancel_order(order_id: str):
    order = order_service.get_order(order_id)

    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    
    try:
        order.cancel_order()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    return {"message": f"Order {order_id} has been cancelled successfully"}