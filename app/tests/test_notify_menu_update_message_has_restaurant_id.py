import pytest
from app.services.notification_service import NotificationService
from app.repositories.notification_repository import NotificationRepository

@pytest.fixture
def service():
    repo = NotificationRepository()
    return NotificationService(repo=repo)

def test_notify_menu_update_message_has_restaurant_id(service):
    n = service.notify_users_of_menu_update("rest_1", "Burger")
    assert "rest_1" in n.message