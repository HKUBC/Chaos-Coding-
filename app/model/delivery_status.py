from enum import Enum

class DeliveryStatus(Enum):
    """
    Enum representing the valid states of a delivery.
    """

    PENDING    = "pending"
    DELIVERING = "delivering"
    DELIVERED  = "delivered"
    CANCELLED  = "cancelled"

    def can_update(self) -> bool:
        return self != DeliveryStatus.CANCELLED and self != DeliveryStatus.DELIVERED
        # The delivery status can be updated if it's not already cancelled or delivered