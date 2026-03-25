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

# ----- Test cases for Order class -----
def test_update_status(order):
    order.update_status(OrderStatus.PREPARING)
    assert order.status == OrderStatus.PREPARING