import pytest
from app.services.auth_service import AuthService


def test_signup_duplicate_raises_error():
    auth = AuthService()
    auth.sign_up("user1", "password123")
    with pytest.raises(ValueError):
        auth.sign_up("user1", "otherpassword")
