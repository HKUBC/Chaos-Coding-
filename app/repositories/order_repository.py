import pandas as pd
import os


class OrderRepository:
    def __init__(self):
        current_dir = os.path.dirname(__file__)
        data_path = os.path.join(current_dir, "..", "data", "food_delivery.csv")
        self.df = pd.read_csv(data_path)
        self._session_orders: dict[str, list] = {}  # This will store orders in memory for the duration of the session, keyed by customer_id

    # Creates a new order by using an order_id
    def get_order_by_id(self, order_id: str):
        for orders in self._session_orders.values():
            for order in orders:
                if order.order_id == order_id:
                    return order
                
        return None

    # Retrieves all orders associated with a specific customer_id
    def get_orders_by_customer(self, customer_id: str):
        for orders in self._session_orders.values():
            for order in orders:
                if order.customer_id == customer_id:
                    return order
                
        return None
    
    # Retrieves all orders associated with a specific restaurant_id
    def save(self, order) -> None:
        customer_id = order.customer_id
        if customer_id not in self._session_orders:
            self._session_orders[customer_id] = []
        self._session_orders[customer_id].append(order)

    # Retrieves all orders associated with a specific customer_id from the session storage
    def get_session_orders(self, customer_id: str) -> list:
        return self._session_orders.get(customer_id, [])