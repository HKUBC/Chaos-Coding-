from app.model.delivery import Delivery
from app.repositories.delivery_repository import DeliveryRepository
from app.model.order import Order

# Shared repository — all service instances use the same in-memory store
_repo = DeliveryRepository()

class DeliveryService:
    
    
    def __init__(self):
        self.repo = _repo

    # Assigns a delivery to an order if the order is in the PREPARING status and doesn't already have a delivery assigned
    def assign_delivery(self, order: Order) -> Delivery | None:
        if order.status.can_deliver():
            if order.order_id in self.repo.deliveries:
                raise ValueError(f"Order {order.order_id} already has a delivery assigned.")
            
            delivery = Delivery(order)
            delivery.delivery_time = self.repo.get_delivery_time(order.order_id)
            delivery.delivery_distance = self.repo.get_delivery_distance(order.order_id)

            self.repo.deliveries[order.order_id] = delivery
            return delivery
        else:
            raise ValueError(f"Can't assign a delivery to an order that is currently {order.status}.")
    
    # Retrieves the delivery for a given order id
    def get_delivery(self, order_id: str) -> Delivery | None:
        return self.repo.deliveries.get(order_id, None)
    
    # Retrieves all deliveries
    def get_all_deliveries(self) -> list:
        return list(self.repo.deliveries.values())

    # Retrieves the delivery time for a given order id
    def get_delivery_time(self, order_id: str) -> int | None:
        return self.repo.get_delivery_time(order_id)
    
    # Retrieves the delivery distance for a given order id
    def get_delivery_distance(self, order_id: str) -> int | None:
        return self.repo.get_delivery_distance(order_id)