import pytest
from unittest.mock import MagicMock, patch
from app.model.order import Order
from app.model.order_status import OrderStatus
from app.services.delivery_service import DeliveryService

# ----- Fixtures for examples and reusable tests -----
@pytest.fixture
def order_example():
    order = MagicMock(spec=Order)
    order.order_id = "001"
    order.status = OrderStatus.PREPARING
    return order

@pytest.fixture
def delivery_service():
    return DeliveryService()

# ----- Test cases for DeliveryService class -----
# Test that the delivery_time method returns the correct delivery for a valid order
def test_delivery_time_with_valid_id(delivery_service, order_example):
    with patch("app.services.delivery_service.repo") as mock_repo:
        mock_repo.deliveries = {}
        mock_repo.get_delivery_time.return_value = 25
        delivery_service.assign_delivery(order_example)
        delivery_time = delivery_service.get_delivery_time(order_example.order_id)
        assert delivery_time == 25

# Test that the delivery_time method returns None for an invalid order id
def test_delivery_time_with_invalid_id(delivery_service):
    with patch("app.services.delivery_service.repo") as mock_repo:
        mock_repo.deliveries = {}
        mock_repo.get_delivery_time.return_value = None
        delivery_time = delivery_service.get_delivery_time("invalid_id")
        assert delivery_time is None