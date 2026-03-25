from datetime import datetime, timezone
from enum import Enum

#This file defines the Notification model which represents a single notification sent to a user or restaurant. 
#It includes the notification type, message, metadata, timestamp, and read status.
class NotificationType(Enum):
    ORDER_RECEIVED    = "order_received"
    ORDER_STATUS      = "order_status"
    PAYMENT_PROCESSED = "payment_processed"
    PAYMENT_DECLINED  = "payment_declined"
    MENU_UPDATED      = "menu_updated"


class Notification:
  
    def __init__(
        self,
        notification_id: str,
        recipient_id: str,          # customer_id OR restaurant_id
        recipient_type: str,        # customer or restaurant, who is receiving this notification
        notification_type: NotificationType,
        message: str,
        metadata: dict = None,
    ):
        if not message:
            raise ValueError("Notification message cannot be empty.")

        self.notification_id   = notification_id
        self.recipient_id      = recipient_id
        self.recipient_type    = recipient_type
        self.notification_type = notification_type
        self.message           = message
        self.metadata          = metadata or {}
        self.timestamp         = datetime.now(timezone.utc).isoformat()
        self.read              = False


    def to_dict(self) -> dict:
        return {
            "notification_id":   self.notification_id,
            "recipient_id":      self.recipient_id,
            "recipient_type":    self.recipient_type,
            "notification_type": self.notification_type.value,
            "message":           self.message,
            "metadata":          self.metadata,
            "timestamp":         self.timestamp,
            "read":              self.read,
        }

    def __repr__(self):
        return (
            f"Notification(id={self.notification_id!r}, "
            f"type={self.notification_type.value!r}, "
            f"recipient={self.recipient_id!r})"
        )