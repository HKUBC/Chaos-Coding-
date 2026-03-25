from app.model.user_role import UserRole
from app.services.auth_service import AuthService


def test_password_login_still_works_after_hashing():
    auth = AuthService()
    auth.sign_up("user1", "mysecretpass", UserRole.CUSTOMER)
    token = auth.login("user1", "mysecretpass")
    assert isinstance(token, str) and len(token) > 0
