from app.services.auth_service import AuthService
from app.model.user_role import UserRole


def test_signup_stores_role():
    auth = AuthService()
    auth.sign_up("user1", "pass123", UserRole.CUSTOMER)
    assert auth._roles["user1"] == UserRole.CUSTOMER
