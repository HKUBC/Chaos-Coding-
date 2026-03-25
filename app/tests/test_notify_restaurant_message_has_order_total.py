def test_notify_restaurant_message_has_order_total(service):
    n = service.notify_restaurant_of_order("r42", "o1", "c5", 49.50)
    assert "49.50" in n.message
