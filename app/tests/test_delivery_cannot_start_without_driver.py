import pytest
from app.model.delivery import Delivery
from app.model.order import Order
from app.model.order_status import OrderStatus
from app.model.delivery_status import DeliveryStatus

def test_delivery_cannot_start_without_driver():
    order = Order("o1", "cust_1", "rest_1")
    order.status = OrderStatus.PENDING
    delivery = Delivery(order)
    with pytest.raises(ValueError):
        delivery.update_status(DeliveryStatus.DELIVERING)