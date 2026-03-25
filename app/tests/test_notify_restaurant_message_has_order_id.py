def test_notify_restaurant_message_has_order_id(service):
    n = service.notify_restaurant_of_order("r42", "order-XYZ", "c5", 29.99)
    assert "order-XYZ" in n.message
