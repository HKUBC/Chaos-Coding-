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