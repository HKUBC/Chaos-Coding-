from enum import Enum

class OrderStatus(Enum):
    """
    Enum representing the valid states of an order.
    """

    CREATING   = "creating"
    PENDING    = "pending"
    PREPARING  = "preparing"
    DELIVERING = "delivering"
    DELIVERED  = "delivered"
    CANCELLED  = "cancelled"

    def can_start(self) -> bool:
        return self == OrderStatus.CREATING
    
    def can_cancel(self) -> bool:
        return self in (OrderStatus.PENDING, OrderStatus.PREPARING)