import pytest
from app.model.notification import Notification, NotificationType


def test_notification_model_empty_message_raises():
    with pytest.raises(ValueError):
        Notification("n1", "r1", "restaurant", NotificationType.ORDER_RECEIVED, "")
