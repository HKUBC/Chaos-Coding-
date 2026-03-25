from app.services.auth_service import AuthService


def test_validate_token_returns_user_id():
    auth = AuthService()
    auth.sign_up("user1", "pass123")
    token = auth.login("user1", "pass123")
    assert auth.validate_token(token) == "user1"
