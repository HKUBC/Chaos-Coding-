import pytest
from unittest.mock import MagicMock
from app.model.order import Order
from app.model.order_status import OrderStatus
from app.model.delivery import Delivery
from app.model.delivery_status import DeliveryStatus

# ----- Fixtures for examples and reusable tests -----
@pytest.fixture
def order_example():
    order = MagicMock(spec=Order)
    order.status = OrderStatus.PENDING
    return order

@pytest.fixture
def delivery(order_example):
    return Delivery(delivery_id="001", order=order_example)

# ----- Test cases for Delivery class -----
def test_update_status_to_delivering(delivery):
    delivery.update_status(DeliveryStatus.DELIVERING)
    assert delivery.status == DeliveryStatus.DELIVERING

def test_update_status_to_delivered(delivery):
    delivery.update_status(DeliveryStatus.DELIVERED)
    assert delivery.status == DeliveryStatus.DELIVERED

def test_update_status_to_cancelled(delivery):
    delivery.update_status(DeliveryStatus.CANCELLED)
    assert delivery.status == DeliveryStatus.CANCELLED

def test_update_status_after_delivered(delivery):
    delivery.update_status(DeliveryStatus.DELIVERED)
    with pytest.raises(ValueError, match="Can't update delivery status. Your delivery is currently DeliveryStatus.DELIVERED."):
        delivery.update_status(DeliveryStatus.CANCELLED)