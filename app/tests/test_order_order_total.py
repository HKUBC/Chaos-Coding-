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
# Tests for order_total
def test_order_total(order, item_example):
    order.add_item(item_example)
    total = order.order_total()
    assert total == item_example.total_price()

def test_order_total_empty(order):
    assert order.order_total() == 0.0

def teset_order_total_multiple_items(order, item_example):
    item_example2 = MagicMock(spec=Item)
    item_example2.item_id = "def"
    item_example2.total_price.return_value = 4.99

    order.add_item(item_example)
    order.add_item(item_example2)
    total = order.order_total()

    assert total == item_example.total_price() + item_example2.total_price()