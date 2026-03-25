from app.model.notification import Notification, NotificationType


def test_notification_repo_save_and_retrieve(repo):
    n = Notification("n1", "r1", "restaurant", NotificationType.ORDER_RECEIVED, "msg")
    repo.save(n)
    assert len(repo.get_for_recipient("r1")) == 1
