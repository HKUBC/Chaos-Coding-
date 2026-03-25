import pytest
from app.services.auth_service import AuthService


def test_login_unknown_user_raises_error():
    auth = AuthService()
    with pytest.raises(ValueError):
        auth.login("nonexistent_user", "anypassword")
