from app.model.notification import Notification, NotificationType


def test_notification_repo_isolated_between_recipients(repo):
    n1 = Notification("n1", "r1", "restaurant", NotificationType.ORDER_RECEIVED, "msg")
    n2 = Notification("n2", "r2", "restaurant", NotificationType.ORDER_RECEIVED, "msg")
    repo.save(n1)
    repo.save(n2)
    assert len(repo.get_for_recipient("r1")) == 1
    assert len(repo.get_for_recipient("r2")) == 1
