import pytest
from app.model.delivery import Delivery
from app.model.order import Order
from app.model.order_status import OrderStatus
from app.model.driver import Driver

def test_driver_assign_duplicate_raises():
    order = Order("o1", "cust_1", "rest_1")
    order.status = OrderStatus.PENDING
    delivery = Delivery(order)
    driver = Driver(driver_id="d1", name="John")
    delivery.assign_driver(driver)
    with pytest.raises(ValueError):
        delivery.assign_driver(driver)