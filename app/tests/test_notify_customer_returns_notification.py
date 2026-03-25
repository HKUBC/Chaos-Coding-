from app.model.notification import Notification


def test_notify_customer_returns_notification(service):
    n = service.notify_user_of_order_status("c1", "o1", "pending")
    assert isinstance(n, Notification)
