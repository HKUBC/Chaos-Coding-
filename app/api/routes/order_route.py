from fastapi import APIRouter, HTTPException
from app.model.item import Item
from app.model.order import Order
from app.model.order_status import OrderStatus
from app.services.delivery_service import DeliveryService
from app.services.order_service import OrderService

router = APIRouter(prefix="/ordering", tags=["Ordering"])
delivery_service = DeliveryService()
order_service = OrderService()

@router.post("/{order_id}/add_item")
def add_item(order_id: str, item: Item):
    order = order_service.get_order(order_id)

    if order is None:
        raise HTTPException(status_code = 404, details = "Order not found")
    
    try:
        order.add_item(item)
    except ValueError as e:
        raise HTTPException(status_code = 400, details = str(e))
    
    return {"message": f"Item {item.name} added to order {order_id}"}

@router.delete("/{order_id}/remove_item")
def remove_item(order_id: str, item: Item):
    order = order_service.get_order(order_id)

    if order is None:
        raise HTTPException(status_code = 404, details = "Order not found")
    
    try:
        order.remove_item(item)
    except ValueError as
