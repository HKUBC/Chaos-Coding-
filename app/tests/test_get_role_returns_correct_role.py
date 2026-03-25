from app.services.auth_service import AuthService
from app.model.user_role import UserRole


def test_get_role_returns_correct_role():
    auth = AuthService()
    auth.sign_up("owner1", "pass123", UserRole.RESTAURANT_OWNER)
    token = auth.login("owner1", "pass123")
    assert auth.get_role(token) == UserRole.RESTAURANT_OWNER
