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
# Tests with start_order
def test_start_order(order, item_example):
    order.add_item(item_example)
    order.start_order()
    assert order.status == OrderStatus.PENDING

def test_start_order_no_items(order):
    with pytest.raises(ValueError, match="Cannot start your order with no items."):
        order.start_order()

def test_start_order_invalid_status(order, item_example):
    order.add_item(item_example)
    order.update_status(OrderStatus.PENDING)
    with pytest.raises(ValueError, match="Cannot start your order. Your order is currently OrderStatus.PENDING."):
        order.start_order()