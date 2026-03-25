from app.services.auth_service import AuthService


def test_signup_stores_credentials():
    auth = AuthService()
    auth.sign_up("user1", "password123")
    # login succeeds without error — credentials were stored
    result = auth.login("user1", "password123")
    assert result == "user1"
