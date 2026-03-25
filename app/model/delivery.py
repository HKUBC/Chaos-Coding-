from app.model import driver
from app.model.order import Order
from app.model.order_status import OrderStatus
from app.model.delivery_status import DeliveryStatus

class Delivery:
    def __init__(self, order: Order):
        if order.status == OrderStatus.CREATING:
            raise ValueError("Can't assign a delivery to an order that hasn't been placed yet.")
        # The delivery can only be assigned to an order that has been placed

        self.delivery_id = order.order_id
        self.order       = order
        self.status      = DeliveryStatus.PENDING
        self.driver      = None

    def update_status(self, new_status: DeliveryStatus):
        if not self.status.can_update():
            raise ValueError(f"Can't update delivery status. Your delivery is currently {self.status}.")
        # The delivery status can only be updated if it's not already cancelled or delivered. For example,
        # you can't update the status of a cancelled delivery to delivering or delivered.
        if new_status == DeliveryStatus.DELIVERING and self.driver is None:
            raise ValueError("A driver must be assigned before the delivery can start.")
        
        self.status = new_status
        # The delivery status can be updated if it's not already cancelled or delivered


    # The driver can only be assigned if the delivery is not cancelled and doesn't already have a driver assigned
    def assign_driver(self, driver):
        if self.status == DeliveryStatus.CANCELLED:
            raise ValueError("Cannot assign a driver to a cancelled delivery.")
        if self.driver is not None:
            raise ValueError("A driver is already assigned to this delivery.")
        self.driver = driver