def test_notify_restaurant_unique_notification_ids(service):
    n1 = service.notify_restaurant_of_order("r42", "o1", "c5", 10.0)
    n2 = service.notify_restaurant_of_order("r42", "o2", "c5", 20.0)
    assert n1.notification_id != n2.notification_id
