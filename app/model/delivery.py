from app.model.order import Order
from app.model.order_status import OrderStatus
from app.model.delivery_status import DeliveryStatus

class Delivery:
    def __init__(self, delivery_id: int, order: Order):
        if order.status == OrderStatus.CREATING:
            raise ValueError("Can't assign a delivery to an order that hasn't been placed yet.")
        # The delivery can only be assigned to an order that has been placed

        self.delivery_id = delivery_id
        self.order = order
        self.status = DeliveryStatus.PENDING

    def update_status(self, new_status: DeliveryStatus):
        if not self.status.can_update():
            raise ValueError(f"Can't update delivery status. Your delivery is currently {self.status}.")
        
        self.status = new_status
        # The delivery status can be updated if it's not already cancelled or delivered