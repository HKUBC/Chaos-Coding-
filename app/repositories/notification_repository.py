from app.model.notification import Notification

class NotificationRepository:
    """
    In-memory store for notifications.
    Key: recipient_id → list of Notification objects.
    """

    def __init__(self):
        self._store: dict[str, list[Notification]] = {}

    def save(self, notification: Notification) -> None:
        recipient = notification.recipient_id
        if recipient not in self._store:
            self._store[recipient] = []
        self._store[recipient].append(notification)

    def get_for_recipient(self, recipient_id: str) -> list[Notification]:
        return self._store.get(recipient_id, [])


    def clear(self) -> None:
        """Utility used in tests to reset state between runs."""
        self._store.clear()