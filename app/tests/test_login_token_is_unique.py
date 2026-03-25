from app.model.user_role import UserRole
from app.services.auth_service import AuthService


def test_login_token_is_unique():
    auth = AuthService()
    auth.sign_up("user1", "pass123", UserRole.CUSTOMER)
    token1 = auth.login("user1", "pass123")
    token2 = auth.login("user1", "pass123")
    assert token1 != token2
