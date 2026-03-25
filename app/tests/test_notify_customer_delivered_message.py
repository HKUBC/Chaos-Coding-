def test_notify_customer_delivered_message(service):
    n = service.notify_user_of_order_status("c1", "o1", "delivered")
    assert "delivered" in n.message.lower()
