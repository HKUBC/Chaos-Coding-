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
    order.order_id = "001"
    order.status = OrderStatus.PENDING
    return order

# ----- Test cases for Delivery class -----
# Test that a delivery can be created with a valid order
def test_delivery_with_valid_order(order_example):
    delivery = Delivery(order=order_example)
    assert delivery.order == order_example

# Test that a delivery cannot be created with an invalid order
def test_delivery_with_invalid_order():
    order_example.status = OrderStatus.CREATING
    with pytest.raises(ValueError, match="Can't assign a delivery to an order that hasn't been placed yet."):
        Delivery(order=order_example)

def test_delivery_id_matches_order_id(order_example):
    delivery = Delivery(order=order_example)
    assert delivery.delivery_id == order_example.order_id