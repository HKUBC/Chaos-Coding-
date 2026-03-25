import pytest
from app.model.order import Order
from app.services.auth_service import AuthService
from app.services.order_service import OrderService


def test_place_order_without_token_raises_error():
    auth = AuthService()
    service = OrderService(auth_service=auth)
    order = Order("o1", "customer1", "r1")
    with pytest.raises(ValueError):
        service.place_order(order)
