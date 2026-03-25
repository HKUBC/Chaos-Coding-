def test_notify_customer_metadata_has_order_id(service):
    n = service.notify_user_of_order_status("c1", "o1", "pending")
    assert n.metadata["order_id"] == "o1"
