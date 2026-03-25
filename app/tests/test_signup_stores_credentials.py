from app.model.user_role import UserRole
from app.services.auth_service import AuthService


def test_signup_stores_credentials():
    auth = AuthService()
    auth.sign_up("user1", "password123", UserRole.CUSTOMER)
    # login succeeds without error — credentials were stored
    token = auth.login("user1", "password123")
    assert isinstance(token, str) and len(token) > 0
