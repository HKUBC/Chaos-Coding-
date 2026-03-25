def test_notify_restaurant_get_notifications_returns_dicts(service):
    service.notify_restaurant_of_order("r42", "o1", "c5", 29.99)
    result = service.get_notifications("r42")
    assert isinstance(result[0], dict)
