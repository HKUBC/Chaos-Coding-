def test_notify_customer_metadata_has_new_status(service):
    n = service.notify_user_of_order_status("c1", "o1", "preparing")
    assert n.metadata["new_status"] == "preparing"
