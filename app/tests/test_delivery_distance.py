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
# Test that the delivery_distance method returns the correct delivery for a valid order
def test_delivery_distance_with_valid_id(delivery_service, order_example):
    service = DeliveryService()

    with patch.object(service.repo, "get_delivery_distance", return_value=10):
        service.assign_delivery(order_example)

        delivery_distance = service.get_delivery_distance(order_example.order_id)

        assert delivery_distance == 10

# Test that the delivery_distance method returns None for an invalid order id
def test_delivery_distance_with_invalid_id():
    service = DeliveryService()

    with patch.object(service.repo, "get_delivery_distance", return_value=None):
        delivery_distance = service.get_delivery_distance("invalid_id")

        assert delivery_distance is None