def test_notify_customer_saved_to_repo(service, repo):
    service.notify_user_of_order_status("c1", "o1", "pending")
    assert len(repo.get_for_recipient("c1")) == 1
