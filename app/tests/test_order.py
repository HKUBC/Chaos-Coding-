import pytest
from unittest.mock import MagicMock
from app.model.item import Item
from app.model.order import Order
from app.model.order_status import OrderStatus

# ----- Fixtures for examples and reusable tests -----
@pytest.fixture
def mock_data_service():
    service = MagicMock()
    service.load_data.return_value = [
        {},
        {"delivery_time": "25 minutes"}
    ]

    return service

@pytest.fixture
def order(mock_data_service):
    """An Order instance for testing."""
    return Order(
        order_id="123",
        customer_id="456",
        restaurant_id="789",
        data_service=mock_data_service,
        notification_service=None,
    )

@pytest.fixture
def item_example():
    item = MagicMock(spec=Item)
    item.item_id = "abc"
    item.total_price.return_value = 9.99
    return item

# ----- Test cases for Order class -----
# Tests for add_item
def test_add_item(order, item_example):
    order.add_item(item_example)
    assert item_example in order.items

def test_add_item_invalid_status(order, item_example):
    order.update_status(OrderStatus.PENDING)
    with pytest.raises(ValueError, match="Cannot add item. Your order is currently OrderStatus.PENDING."):
        order.add_item(item_example)

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

# Tests for get_item
def test_get_item(order, item_example):
    order.add_item(item_example)
    retrieved_item = order.get_item(item_example.item_id)
    assert retrieved_item == item_example

def test_get_item_not_found(order):
    assert order.get_item("nonexistent_id") is None

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

def test_update_status(order):
    order.update_status(OrderStatus.PREPARING)
    assert order.status == OrderStatus.PREPARING

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