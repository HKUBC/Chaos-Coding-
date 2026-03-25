def test_notify_customer_multiple_updates_saved(service, repo):
    service.notify_user_of_order_status("c1", "o1", "pending")
    service.notify_user_of_order_status("c1", "o1", "preparing")
    service.notify_user_of_order_status("c1", "o1", "delivered")
    assert len(repo.get_for_recipient("c1")) == 3
