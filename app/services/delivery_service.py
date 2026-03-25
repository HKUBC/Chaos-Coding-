from app.model.delivery import Delivery
from app.model.delivery_status import DeliveryStatus
from app.repositories.delivery_repository import DeliveryRepository
from app.model.order import Order
from app.model.order_status import OrderStatus

repo = DeliveryRepository()

class DeliveryService:
    """
    Responsible for manging the deliveries and ensures that each order has at most one delivery.
    """

    # Assigns a delivery to an order if the order is in the PREPARING status and doesn't already have a delivery assigned
    def assign_delivery(self, order: Order) -> Delivery | None:
        if order.status.can_deliver():
            if order.order_id in repo.deliveries:
                raise ValueError(f"Order {order.order_id} already has a delivery assigned.")
            
            delivery = Delivery(order)
            repo.deliveries[order.order_id] = delivery
            return delivery
        else:
            raise ValueError(f"Can't assign a delivery to an order that is currently {order.status}.")
    
    # Retrieves the delivery for a given order id
    def get_delivery(self, order_id: str) -> Delivery | None:
        return repo.deliveries.get(order_id, None)
    
    # Retrieves the delivery time for a given order id
    def get_delivery_time(self, order_id: str) -> int | None:
        return repo.get_delivery_time(order_id)
    
    # Retrieves the delivery distance for a given order id
    def get_delivery_distance(self, order_id: str) -> int | None:
        return repo.get_delivery_distance(order_id)