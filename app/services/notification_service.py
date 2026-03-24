import uuid
from app.model.notification import Notification, NotificationType
from app.repositories.notification_repository import NotificationRepository

class NotificationService:
    """
    Central service for creating and dispatching notifications.
    Issue #43: notify_restaurant_of_order
    """

    def __init__(self, repo: NotificationRepository = None):
        self._repo = repo or NotificationRepository()


    def notify_restaurant_of_order(
        self,
        restaurant_id: str,
        order_id: str,
        customer_id: str,
        order_total: float,
    ) -> Notification:
        """
        Called after payment is confirmed. Sends a new-order alert
        to the restaurant.
        """
        notification = Notification(
            notification_id=str(uuid.uuid4()),
            recipient_id=restaurant_id,
            recipient_type="restaurant",
            notification_type=NotificationType.ORDER_RECEIVED,
            message=(
                f"New order #{order_id} received from customer "
                f"{customer_id}. Total: ${order_total:.2f}."
            ),
            metadata={
                "order_id":    order_id,
                "customer_id": customer_id,
                "order_total": order_total,
            },
        )
        self._repo.save(notification)
        return notification

    def get_notifications(self, recipient_id: str) -> list[dict]:
        return [n.to_dict() for n in self._repo.get_for_recipient(recipient_id)]
