import pytest
from app.services.notification_service import NotificationService
from app.repositories.notification_repository import NotificationRepository
from app.model.notification import NotificationType

@pytest.fixture
def service():
    repo = NotificationRepository()
    return NotificationService(repo=repo)

def test_notify_menu_update_type(service):
    n = service.notify_users_of_menu_update("rest_1", "Burger")
    assert n.notification_type == NotificationType.MENU_UPDATED