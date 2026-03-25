def test_notify_customer_unknown_status(service):
    n = service.notify_user_of_order_status("c1", "o1", "unknown_status")
    assert "unknown_status" in n.message.lower()
