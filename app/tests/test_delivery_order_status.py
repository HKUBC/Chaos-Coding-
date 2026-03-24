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
def test_delivery_initialization_with_valid_order(delivery, order_example):
    assert delivery.order == order_example

def test_delivery_initialization_with_invalid_order():
    order = MagicMock(spec=Order)
    order.status = OrderStatus.CREATING
    with pytest.raises(ValueError, match="Can't assign a delivery to an order that hasn't been placed yet."):
        Delivery(delivery_id="002", order=order)