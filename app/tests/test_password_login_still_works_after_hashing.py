from app.services.auth_service import AuthService


def test_password_login_still_works_after_hashing():
    auth = AuthService()
    auth.sign_up("user1", "mysecretpass")
    result = auth.login("user1", "mysecretpass")
    assert result == "user1"
