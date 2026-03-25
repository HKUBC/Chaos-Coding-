def test_notify_customer_cancelled_message(service):
    n = service.notify_user_of_order_status("c1", "o1", "cancelled")
    assert "cancelled" in n.message.lower()
