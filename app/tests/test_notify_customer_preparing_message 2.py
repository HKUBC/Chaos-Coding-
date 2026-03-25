def test_notify_customer_preparing_message(service):
    n = service.notify_user_of_order_status("c1", "o1", "preparing")
    assert "prepared" in n.message.lower()
