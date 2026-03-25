from app.model.user_role import UserRole
import pytest
from app.services.auth_service import AuthService


def test_token_invalidated_after_logout():
    auth = AuthService()
    auth.sign_up("user1", "pass123", UserRole.CUSTOMER)
    token = auth.login("user1", "pass123")
    auth.logout(token)
    with pytest.raises(ValueError):
        auth.validate_token(token)
