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
# Test that a delivery can be assigned to a valid order
def test_assign_delivery_with_valid_order(delivery_service, order_example):
    service = DeliveryService()

    order_example.status = OrderStatus.PREPARING

    with patch.object(service.repo, "get_delivery_time", return_value=25), \
         patch.object(service.repo, "get_delivery_distance", return_value=10):

        delivery = service.assign_delivery(order_example)

        assert delivery.order == order_example
        assert delivery.delivery_time == 25
        assert delivery.delivery_distance == 10

# Test that a delivery cannot be assigned to an invalid order
def test_assign_delivery_with_invalid_status(delivery_service, order_example):
    service = DeliveryService()

    order_example.status = OrderStatus.PENDING

    with pytest.raises(ValueError, match="Can't assign a delivery to an order that is currently"):
        service.assign_delivery(order_example)

# Test that a delivery cannot be assigned to an order that already has a delivery
def test_assign_delivery_to_order_with_existing_delivery(delivery_service, order_example):
    service = DeliveryService()

    order_example.status = OrderStatus.PREPARING

    with patch.object(service.repo, "get_delivery_time", return_value=25), \
         patch.object(service.repo, "get_delivery_distance", return_value=10):

        service.assign_delivery(order_example)

        with pytest.raises(ValueError, match=f"Order {order_example.order_id} already has a delivery assigned."):
            service.assign_delivery(order_example)