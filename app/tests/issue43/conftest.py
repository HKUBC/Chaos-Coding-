import pytest
from app.repositories.notification_repository import NotificationRepository
from app.services.notification_service import NotificationService


@pytest.fixture
def repo():
    return NotificationRepository()


@pytest.fixture
def service(repo):
    return NotificationService(repo=repo)
