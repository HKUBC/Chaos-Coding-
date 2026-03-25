import pytest
from app.services.notification_service import NotificationService
from app.repositories.notification_repository import NotificationRepository

@pytest.fixture
def service():
    repo = NotificationRepository()
    return NotificationService(repo=repo)

def test_notify_payment_unique_ids(service):
    n1 = service.notify_user_of_payment("cust_1", "order_1", 10.0, approved=True)
    n2 = service.notify_user_of_payment("cust_1", "order_2", 10.0, approved=True)
    assert n1.notification_id != n2.notification_id