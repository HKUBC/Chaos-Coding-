from fastapi import APIRouter, HTTPException
from app.model.order import Order
from app.model.order_status import OrderStatus
from app.services.delivery_service import DeliveryService
from app.services.order_service import OrderService

router = APIRouter(prefix="/deliveries")
delivery_service = DeliveryService()
order_service = OrderService()

@router.post("/{order_id}/assign")
# this route method will assign a delivery to an order
def assign_delivery(order_id: str):
    order = order_service.get_order(order_id)

    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")

    order = Order(
        order_id=order["order_id"],
        customer_id=order["customer_id"],
        restaurant_id=order["restaurant_id"]
    )
    order.update_status(OrderStatus.PREPARING)

    try:
        delivery = delivery_service.assign_delivery(order)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {"message": "Delivery assigned successfully to order {order_id}"}

@router.get("/{order_id}")
# this route method will get the delivery details for a given order id
def get_delivery(order_id: str):
    delivery = delivery_service.get_delivery(order_id)
    
    if delivery is None:
        raise HTTPException(status_code=404, detail="Delivery not found")

    return {"delivery_id": delivery.delivery_id}

@router.get("/{order_id}/time")
# this route method will get the estimated delivery time for a given order id
def get_delivery_time(order_id: str):
    time = delivery_service.get_delivery_time(order_id)

    if time is None:
        raise HTTPException(status_code=404, detail="Delivery not found")

    return {"delivery_time": time}

@router.get("/{order_id}/distance")
# this route method will get the estimated delivery distance for a given order id
def get_delivery_distance(order_id: str):
    distance = delivery_service.get_delivery_distance(order_id)

    if distance is None:
        raise HTTPException(status_code=404, detail="Delivery not found")

    return {"delivery_distance": distance}

@router.get("/{order_id}/delivery_status")
# this route method will get the status of the delivery for a given order id
def get_delivery_status(order_id: str):
    delivery = delivery_service.get_delivery(order_id)

    if delivery is None:
        raise HTTPException(status_code=404, detail="Delivery not found")

    return {"status": delivery.status.value}

@router.put("/{order_id}/update_status")
# this route method will update the status of the delivery for a given order id
def update_delivery_status(order_id: str, status: str):
    delivery = delivery_service.get_delivery(order_id)

    if delivery is None:
        raise HTTPException(status_code=404, detail="Delivery not found")

    try:
        delivery.status = status
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {"message": f"Delivery status updated successfully to {status} for order {order_id}"}