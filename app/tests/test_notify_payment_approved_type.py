import pytest
from app.services.notification_service import NotificationService
from app.repositories.notification_repository import NotificationRepository
from app.model.notification import NotificationType

@pytest.fixture
def service():
    repo = NotificationRepository()
    return NotificationService(repo=repo)

def test_notify_payment_approved_type(service):
    n = service.notify_user_of_payment("cust_1", "order_99", 42.50, approved=True)
    assert n.notification_type == NotificationType.PAYMENT_PROCESSED