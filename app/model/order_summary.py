from app.model.order import Order

class OrderSummary:
    def __init__(self, order: Order):
        self.order_id = order.order_id
        self.customer_id = order.customer_id
        self.restaurant_id = order.restaurant_id

        self.items = order.items
        self.total_amount = order.order_total()
        
        self.order_date = order.order_date
        self.delivery_address = None # Placeholder for delivery address once customer class is implemented

    def to_dict(self):
        return {
            "order_id": self.order_id,
            "customer_id": self.customer_id,
            "restaurant_id": self.restaurant_id,
            "items": [item.to_dict() for item in self.items],
            "quantity":[item.quantity for item in self.items],
            "total_amount": self.total_amount,
            "order_date": self.order_date,
            "delivery_address": self.delivery_address
        }