from app.model.notification import Notification, NotificationType


def test_notification_model_timestamp_set_on_creation():
    n = Notification("n1", "r1", "restaurant", NotificationType.ORDER_RECEIVED, "msg")
    assert n.timestamp is not None
