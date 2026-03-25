import pytest
from app.services.auth_service import AuthService
from app.model.user_role import UserRole


def test_require_role_raises_error_when_role_wrong():
    auth = AuthService()
    auth.sign_up("customer1", "pass123", UserRole.CUSTOMER)
    token = auth.login("customer1", "pass123")
    with pytest.raises(ValueError):
        auth.require_role(token, UserRole.RESTAURANT_OWNER)
