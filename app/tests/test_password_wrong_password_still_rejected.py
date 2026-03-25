import pytest
from app.services.auth_service import AuthService


def test_password_wrong_password_still_rejected():
    auth = AuthService()
    auth.sign_up("user1", "correctpass")
    with pytest.raises(ValueError):
        auth.login("user1", "wrongpass")
