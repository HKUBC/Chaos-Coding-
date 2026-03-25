import uuid  # Used for generating unique notification IDs
from app.model.notification import Notification, NotificationType
from app.repositories.notification_repository import NotificationRepository

class NotificationService:


    def __init__(self, repo: NotificationRepository = None):
        self._repo = repo or NotificationRepository()


    def notify_restaurant_of_order(
        self,
        restaurant_id: str,
        order_id: str,
        customer_id: str,
        order_total: float,
    ) -> Notification:

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

    def notify_user_of_order_status(
        self,
        customer_id: str,
        order_id: str,
        new_status: str,
    ) -> Notification:
        status_messages = {
            "pending":   f"Your order #{order_id} has been received and is pending confirmation.",
            "preparing": f"Your order #{order_id} is being prepared.",
            "delivered": f"Your order #{order_id} has been delivered. Enjoy your meal!",
            "cancelled": f"Your order #{order_id} has been cancelled.",
        }

        message = status_messages.get(
            new_status.lower(),
            f"Your order #{order_id} status has been updated to: {new_status}."
        )

        notification = Notification(
            notification_id=str(uuid.uuid4()),
            recipient_id=customer_id,
            recipient_type="customer",
            notification_type=NotificationType.ORDER_STATUS,
            message=message,
            metadata={
                "order_id":   order_id,
                "new_status": new_status,
            },
        )
        self._repo.save(notification)
        return notification

    def notify_user_of_order_status(
        self,
        customer_id: str,
        order_id: str,
        new_status: str,
    ) -> Notification:
    
        status_messages = {
            "pending":   f"Your order #{order_id} has been received and is pending confirmation.",
            "preparing": f"Your order #{order_id} is being prepared.",
            "delivered": f"Your order #{order_id} has been delivered. Enjoy your meal!",
            "cancelled": f"Your order #{order_id} has been cancelled.",
        }

        message = status_messages.get(
            new_status.lower(),
            f"Your order #{order_id} status has been updated to: {new_status}."
        )

        notification = Notification(
            notification_id=str(uuid.uuid4()),
            recipient_id=customer_id,
            recipient_type="customer",
            notification_type=NotificationType.ORDER_STATUS,
            message=message,
            metadata={
                "order_id":   order_id,
                "new_status": new_status,
            },
        )
        self._repo.save(notification)
        return notification