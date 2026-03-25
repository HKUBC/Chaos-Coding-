import pandas as pd
import os

class OrderRepository:
    def __init__(self):
        current_dir = os.path.dirname(__file__)
        data_path = os.path.join(current_dir, "..", "data", "food_delivery.csv")
        self.df = pd.read_csv(data_path)

    # Creates a new order by using an order_id
    def get_order_by_id(self, order_id: str):
        return self.df[self.df["order_id"] == order_id]

    # Retrieves all orders associated with a specific customer_id
    def get_orders_by_customer(self, customer_id: str):
        return self.df[self.df["customer_id"] == customer_id]