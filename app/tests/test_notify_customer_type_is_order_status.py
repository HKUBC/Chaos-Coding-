from app.model.notification import NotificationType


def test_notify_customer_type_is_order_status(service):
    n = service.notify_user_of_order_status("c1", "o1", "pending")
    assert n.notification_type == NotificationType.ORDER_STATUS
