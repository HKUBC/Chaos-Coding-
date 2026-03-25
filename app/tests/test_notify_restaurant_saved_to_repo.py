def test_notify_restaurant_saved_to_repo(service, repo):
    service.notify_restaurant_of_order("r42", "o1", "c5", 29.99)
    assert len(repo.get_for_recipient("r42")) == 1
