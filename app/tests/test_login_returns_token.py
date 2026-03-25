from app.services.auth_service import AuthService


def test_login_returns_token():
    auth = AuthService()
    auth.sign_up("user1", "pass123")
    token = auth.login("user1", "pass123")
    assert isinstance(token, str)
    assert len(token) > 0
