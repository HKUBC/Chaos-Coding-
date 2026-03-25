from app.model.user_role import UserRole
from app.services.auth_service import AuthService


def test_login_returns_token():
    auth = AuthService()
    auth.sign_up("user1", "pass123", UserRole.CUSTOMER)
    token = auth.login("user1", "pass123")
    assert isinstance(token, str)
    assert len(token) > 0
