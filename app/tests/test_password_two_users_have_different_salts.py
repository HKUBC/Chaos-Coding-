from app.model.user_role import UserRole
from app.services.auth_service import AuthService


def test_password_two_users_have_different_salts():
    auth = AuthService()
    auth.sign_up("user1", "samepassword", UserRole.CUSTOMER)
    auth.sign_up("user2", "samepassword", UserRole.CUSTOMER)
    salt1, hash1 = auth._credentials["user1"]
    salt2, hash2 = auth._credentials["user2"]
    assert salt1 != salt2
    assert hash1 != hash2
