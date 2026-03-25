from app.model.notification import Notification, NotificationType


def test_notification_repo_clear_removes_all(repo):
    n = Notification("n1", "r1", "restaurant", NotificationType.ORDER_RECEIVED, "msg")
    repo.save(n)
    repo.clear()
    assert repo.get_for_recipient("r1") == []
