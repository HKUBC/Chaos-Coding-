from app.model.user_role import UserRole
from app.model.order import Order
from app.model.item import Item
from app.services.auth_service import AuthService
from app.services.order_service import OrderService


def test_logged_in_user_can_place_order():
    auth = AuthService()
    auth.sign_up("customer1", "pass123", UserRole.CUSTOMER)
    token = auth.login("customer1", "pass123")

    service = OrderService(auth_service=auth)
    order = Order("o1", "customer1", "r1")
    order.add_item(Item(item_id=1, name="Burger", price=10.0))
    result = service.place_order(order, token=token)
    assert result.order_id == "o1"
