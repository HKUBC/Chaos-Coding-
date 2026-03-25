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
# Tests for remove_item
def test_remove_item(order, item_example):
    order.add_item(item_example)
    order.remove_item(item_example.item_id)
    assert item_example not in order.items

def test_remove_item_invalid_status(order, item_example):
    order.add_item(item_example)
    order.update_status(OrderStatus.PREPARING)
    with pytest.raises(ValueError, match="Cannot remove item. Your order is currently OrderStatus.PREPARING"):
        order.remove_item(item_example.item_id)

def test_remove_item_not_found(order, item_example):
    order.add_item(item_example)
    order.remove_item("nonexistent_id")
    assert item_example in order.items