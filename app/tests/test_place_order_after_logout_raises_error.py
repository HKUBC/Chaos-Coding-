from app.model.user_role import UserRole
import pytest
from app.model.order import Order
from app.services.auth_service import AuthService
from app.services.order_service import OrderService


def test_place_order_after_logout_raises_error():
    auth = AuthService()
    auth.sign_up("customer1", "pass123", UserRole.CUSTOMER)
    token = auth.login("customer1", "pass123")
    auth.logout(token)

    service = OrderService(auth_service=auth)
    order = Order("o1", "customer1", "r1")
    with pytest.raises(ValueError):
        service.place_order(order, token=token)
