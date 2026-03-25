from app.model.delivery import Delivery
from app.model.order import Order
from app.model.order_status import OrderStatus
from app.model.delivery_status import DeliveryStatus
from app.model.driver import Driver

def test_delivery_can_update_to_delivered_with_driver():
    order = Order("o1", "cust_1", "rest_1")
    order.status = OrderStatus.PENDING
    delivery = Delivery(order)
    driver = Driver(driver_id="d1", name="John")
    delivery.assign_driver(driver)
    delivery.update_status(DeliveryStatus.DELIVERING)
    delivery.update_status(DeliveryStatus.DELIVERED)
    assert delivery.status == DeliveryStatus.DELIVERED