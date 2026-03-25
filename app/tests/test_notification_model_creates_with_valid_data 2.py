from app.model.notification import Notification, NotificationType


def test_notification_model_creates_with_valid_data():
    n = Notification(
        notification_id="n1",
        recipient_id="r42",
        recipient_type="restaurant",
        notification_type=NotificationType.ORDER_RECEIVED,
        message="New order received.",
    )
    assert n.notification_id == "n1"
    assert n.recipient_id == "r42"
