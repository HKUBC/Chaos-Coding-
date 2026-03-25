import pytest
from app.services.notification_service import NotificationService
from app.repositories.notification_repository import NotificationRepository

@pytest.fixture
def service():
    repo = NotificationRepository()
    return NotificationService(repo=repo)

def test_notify_menu_update_unique_ids(service):
    n1 = service.notify_users_of_menu_update("rest_1", "Burger")
    n2 = service.notify_users_of_menu_update("rest_1", "Pizza")
    assert n1.notification_id != n2.notification_id