import pytest
from app.services.notification_service import NotificationService
from app.repositories.notification_repository import NotificationRepository

@pytest.fixture
def service():
    repo = NotificationRepository()
    return NotificationService(repo=repo)

def test_notify_payment_recipient_is_customer(service):
    n = service.notify_user_of_payment("cust_1", "order_99", 42.50, approved=True)
    assert n.recipient_id == "cust_1"
    assert n.recipient_type == "customer"