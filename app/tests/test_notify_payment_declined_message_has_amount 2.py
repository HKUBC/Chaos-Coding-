import pytest
from app.services.notification_service import NotificationService
from app.repositories.notification_repository import NotificationRepository

@pytest.fixture
def service():
    repo = NotificationRepository()
    return NotificationService(repo=repo)

def test_notify_payment_declined_message_has_amount(service):
    n = service.notify_user_of_payment("cust_1", "order_99", 42.50, approved=False)
    assert "42.50" in n.message