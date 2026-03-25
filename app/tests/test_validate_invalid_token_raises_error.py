import pytest
from app.services.auth_service import AuthService


def test_validate_invalid_token_raises_error():
    auth = AuthService()
    with pytest.raises(ValueError):
        auth.validate_token("not_a_real_token")
