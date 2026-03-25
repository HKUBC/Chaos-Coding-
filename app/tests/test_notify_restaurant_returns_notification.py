from app.model.notification import Notification


def test_notify_restaurant_returns_notification(service):
    n = service.notify_restaurant_of_order("r42", "o1", "c5", 29.99)
    assert isinstance(n, Notification)
