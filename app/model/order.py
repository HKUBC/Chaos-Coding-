from model.item import Item
from model.order_status import OrderStatus
from services.data_service import DataService

class Order:
    """
    Manages order details, including items, and status.
    Dependency on DataService to load delivery data from a CSV file.
    """

    def __init__(self, order_id : str, customer_id : str, restaurant_id : str, data_service: DataService):
        self.order_id          = order_id
        self.customer_id       = customer_id
        self.restaurant_id     = restaurant_id
        
        self.items: list[Item] = []                     # List of items

        self.status            = OrderStatus.CREATING    # Order status: creating, pending, preparing, delivered, cancelled
        self._data_service     = data_service

    def add_item(self, item: Item):
        if self.status != OrderStatus.CREATING:
            raise ValueError(f"Cannot add item. Current order status: {self.status}")
        
        self.items.append(item)

    def remove_item(self, item_id: str) -> Item | None:
        if self.status != OrderStatus.CREATING:
            raise ValueError(f"Cannot remove item. Current order status: {self.status}")
        
        self.items = [item for item in self.items 
                        if item.item_id != item_id]

    def get_item(self, item_id: str) -> Item | None:
        return next((item for item in self.items
                        if item.item_id == item_id), None)
    
    def order_total(self) -> float:
        return sum(item.total_price() for item in self.items)
    
    def update_status(self, new_status: OrderStatus):
        self.status = new_status

    def start_order(self):
        if self.items == []:
            raise ValueError("Cannot start order with no items.")

        if not self.status.can_start():
            raise ValueError(f"Cannot start order. Current status: {self.status}")
        
        delivery_data = self._data_service.load_data()
        if delivery_data:
            row = delivery_data[1]
            print(f"Starting order {self.order_id} with delivery time: ", row.get('delivery_time', 'N/A'))

        self.update_status(OrderStatus.PREPARING)

    def cancel_order(self):
        if not self.status.can_cancel():
            raise ValueError(f"Cannot cancel order. Current status: {self.status}")
        
        self.update_status(OrderStatus.CANCELLED)