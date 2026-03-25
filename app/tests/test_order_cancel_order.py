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

@pytest.fixture
def item_example():
    item = MagicMock(spec=Item)
    item.item_id = "abc"
    item.total_price.return_value = 9.99
    return item

# ----- Test cases for Order class -----
# Tests with cancel_order
def test_cancel_order(order, item_example):
    order.add_item(item_example)
    order.start_order()
    order.cancel_order()
    assert order.status == OrderStatus.CANCELLED

def test_cancel_order_from_preparing(order, item_example):
    order.add_item(item_example)
    order.start_order()
    order.update_status(OrderStatus.PREPARING)
    order.cancel_order()
    assert order.status == OrderStatus.CANCELLED

def test_cancel_order_invalid_status(order, item_example):
    with pytest.raises(ValueError, match="Cannot cancel your order. Your order hasn't been started yet."):
        order.cancel_order()
    
    order.update_status(OrderStatus.DELIVERED)
    with pytest.raises(ValueError, match="Cannot cancel your order. Your order has already been delivered."):
        order.cancel_order()