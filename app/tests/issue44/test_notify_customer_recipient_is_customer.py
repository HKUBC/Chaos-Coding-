def test_notify_customer_recipient_is_customer(service):
    n = service.notify_user_of_order_status("c1", "o1", "pending")
    assert n.recipient_id == "c1"
    assert n.recipient_type == "customer"
