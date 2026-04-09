from app.model.notification import Notification

class NotificationRepository:

    def __init__(self):
        self._store: dict[str, list[Notification]] = {}

    def save(self, notification: Notification) -> None:
        recipient = notification.recipient_id
        if recipient not in self._store:
            self._store[recipient] = []
        self._store[recipient].append(notification)

    def get_for_recipient(self, recipient_id: str) -> list[Notification]:
        return self._store.get(recipient_id, [])


    def mark_read(self, recipient_id: str, notification_id: str) -> None:
        for n in self._store.get(recipient_id, []):
            if n.notification_id == notification_id:
                n.read = True

    def mark_all_read(self, recipient_id: str) -> None:
        for n in self._store.get(recipient_id, []):
            n.read = True

    def get_unread(self, recipient_id: str) -> list[Notification]:
        return [n for n in self._store.get(recipient_id, []) if not n.read]

    def clear(self) -> None:
        self._store.clear()