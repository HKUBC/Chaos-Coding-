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
    order.status = OrderStatus.PENDING
    return order

@pytest.fixture
def delivery_service():
    return DeliveryService()

# ----- Test cases for DeliveryService class -----
# Test that the get_delivery method returns the correct delivery for a valid order
def test_get_delivery_with_valid_id(delivery_service, order_example):
    with patch("app.services.delivery_service.DeliveryRepository") as MockRepo:
        mock_repo_instance = MockRepo.return_value
        mock_repo_instance.deliveries = {}

        order_example.status = OrderStatus.PREPARING

        delivery_service.assign_delivery(order_example)

        delivery = delivery_service.get_delivery(order_example.order_id)

        assert delivery.order == order_example

# Test that the get_delivery method returns None for an invalid order id
def test_get_delivery_with_invalid_id(delivery_service):
    with patch("app.services.delivery_service.DeliveryRepository") as MockRepo:
        mock_repo_instance = MockRepo.return_value
        mock_repo_instance.deliveries = {}

        delivery = delivery_service.get_delivery("invalid_id")

        assert delivery is None