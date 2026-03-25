def test_notify_customer_message_has_order_id(service):
    n = service.notify_user_of_order_status("c1", "order-ABC", "pending")
    assert "order-ABC" in n.message
