import pytest
from unittest.mock import MagicMock
from app.model.item import Item
from app.model.order import Order
from app.model.order_status import OrderStatus

# ----- Fixtures for examples and reusable tests -----
@pytest.fixture
def order():
    """An Order instance for testing."""
    return Order(order_id="123", customer_id="456", restaurant_id="789")

# ----- Test cases for Order class -----
def test_update_status(order):
    order.update_status(OrderStatus.PREPARING)
    assert order.status == OrderStatus.PREPARING