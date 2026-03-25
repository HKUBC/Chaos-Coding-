import pandas as pd
import os

class DeliveryRepository:
    def __init__(self):
        current_dir = os.path.dirname(__file__)
        data_path = os.path.join(current_dir, "..", "data", "food_delivery.csv")

        self.df = pd.read_csv(data_path)
        self.deliveries = {} # order_id = delivery_id

    # Returns the delivery information for a given order id
    def get_delivery_by_order_id(self, order_id: str):
        data = self.df[self.df["order_id"] == order_id]

        if data.empty:
            return None
        return data.iloc[0].to_dict()
        
    # Returns the delivery time for a given order id
    def get_delivery_time(self, order_id: str):
        data = self.get_delivery_by_order_id(order_id)

        if data:
            return data.get("delivery_time", None)
        return None
    
    # Returns the delivery distance for a given order id
    def get_delivery_distance(self, order_id: str):
        data = self.get_delivery_by_order_id(order_id)

        if data:
            return data.get("delivery_distance", None)
        return None
    
