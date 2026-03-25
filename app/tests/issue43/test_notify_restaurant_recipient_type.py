def test_notify_restaurant_recipient_type(service):
    n = service.notify_restaurant_of_order("r42", "o1", "c5", 29.99)
    assert n.recipient_type == "restaurant"
