from app.model.notification import Notification, NotificationType


def test_notification_model_to_dict_type_is_string():
    n = Notification("n1", "r1", "restaurant", NotificationType.ORDER_RECEIVED, "msg")
    assert isinstance(n.to_dict()["notification_type"], str)
