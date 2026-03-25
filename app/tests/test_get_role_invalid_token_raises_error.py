import pytest
from app.services.auth_service import AuthService


def test_get_role_invalid_token_raises_error():
    auth = AuthService()
    with pytest.raises(ValueError):
        auth.get_role("not_a_real_token")
