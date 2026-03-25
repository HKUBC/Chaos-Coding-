from app.services.auth_service import AuthService


def test_login_correct_password_succeeds():
    auth = AuthService()
    auth.sign_up("user1", "securepass")
    result = auth.login("user1", "securepass")
    assert result == "user1"
