import pytest
from app.services.notification_service import NotificationService
from app.repositories.notification_repository import NotificationRepository

@pytest.fixture
def service():
    repo = NotificationRepository()
    return NotificationService(repo=repo)

def test_notify_menu_update_saves_notification(service):
    service.notify_users_of_menu_update("rest_1", "Burger")
    assert len(service.get_notifications("rest_1")) == 1