from app.model.order import Order
from app.model.order_status import OrderStatus
from app.repositories.order_repository import OrderRepository

repo = OrderRepository()

class OrderService:
    # Creates a new order by using an order_id, customer_id, and restaurant_id
    def create_order(self, order_id: str, customer_id: str, restaurant_id: str) -> Order:
        order = Order(order_id, customer_id, restaurant_id)
        return order
    
    # Retrieves an order by its order_id
    def get_order(self, order_id: str) -> Order | None:
        return repo.get_order_by_id(order_id)
    
    # Retrieves all orders associated with a specific customer_id
    def get_orders_by_customer(self, customer_id: str) -> list[Order] | None:
        return repo.get_orders_by_customer(customer_id)