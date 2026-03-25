def test_notification_repo_empty_for_unknown_recipient(repo):
    assert repo.get_for_recipient("nobody") == []
