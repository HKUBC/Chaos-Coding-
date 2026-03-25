from app.model.notification import Notification, NotificationType


def test_notification_model_to_dict_required_keys():
    n = Notification("n1", "r1", "restaurant", NotificationType.ORDER_RECEIVED, "msg")
    d = n.to_dict()
    for key in ("notification_id", "recipient_id", "recipient_type",
                "notification_type", "message", "timestamp"):
        assert key in d
