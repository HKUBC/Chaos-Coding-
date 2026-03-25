from app.model.user_role import UserRole
from app.services.auth_service import AuthService


def test_password_not_stored_as_plaintext():
    auth = AuthService()
    auth.sign_up("user1", "mysecretpass", UserRole.CUSTOMER)
    salt, stored_hash = auth._credentials["user1"]
    assert stored_hash != "mysecretpass"
