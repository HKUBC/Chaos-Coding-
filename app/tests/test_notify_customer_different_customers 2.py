def test_notify_customer_different_customers(service, repo):
    service.notify_user_of_order_status("c1", "o1", "pending")
    service.notify_user_of_order_status("c2", "o2", "pending")
    assert len(repo.get_for_recipient("c1")) == 1
    assert len(repo.get_for_recipient("c2")) == 1
