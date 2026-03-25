from app.model.notification import NotificationType


def test_notify_restaurant_type_is_order_received(service):
    n = service.notify_restaurant_of_order("r42", "o1", "c5", 29.99)
    assert n.notification_type == NotificationType.ORDER_RECEIVED
