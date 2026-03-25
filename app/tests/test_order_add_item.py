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
    return Order(order_id="123", customer_id="456", restaurant_id="789", data_service=mock_data_service)

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