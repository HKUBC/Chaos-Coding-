from app.services.auth_service import AuthService
from app.model.user_role import UserRole


def test_require_role_passes_when_role_matches():
    auth = AuthService()
    auth.sign_up("driver1", "pass123", UserRole.DRIVER)
    token = auth.login("driver1", "pass123")
    # should not raise
    auth.require_role(token, UserRole.DRIVER)
