import pytest
from app.services.auth_service import AuthService


def test_login_wrong_password_raises_error():
    auth = AuthService()
    auth.sign_up("user1", "correctpass")
    with pytest.raises(ValueError):
        auth.login("user1", "wrongpass")
