from app.model.notification import Notification, NotificationType


def test_notification_repo_multiple_same_recipient(repo):
    for i in range(3):
        n = Notification(str(i), "r1", "restaurant", NotificationType.ORDER_RECEIVED, "msg")
        repo.save(n)
    assert len(repo.get_for_recipient("r1")) == 3
