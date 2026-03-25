def test_notify_customer_unique_notification_ids(service):
    n1 = service.notify_user_of_order_status("c1", "o1", "pending")
    n2 = service.notify_user_of_order_status("c1", "o1", "preparing")
    assert n1.notification_id != n2.notification_id
