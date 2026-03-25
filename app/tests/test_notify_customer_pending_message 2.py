def test_notify_customer_pending_message(service):
    n = service.notify_user_of_order_status("c1", "o1", "pending")
    assert "pending" in n.message.lower()
