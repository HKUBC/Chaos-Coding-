from app.model.item import Item
from app.model.order_status import OrderStatus

class Order:
    """
    Manages order details, including items, and status.
    """

    def __init__(self, order_id: str, customer_id: str, restaurant_id: str, notification_service = None):
        self.order_id          = order_id
        self.customer_id       = customer_id
        self.restaurant_id     = restaurant_id

        self.items: list[Item] = []
        self.status            = OrderStatus.CREATING

        self._notification_service = notification_service

    def add_item(self, item: Item):
        if self.status != OrderStatus.CREATING:
            raise ValueError(f"Cannot add item. Your order is currently {self.status}.")
        self.items.append(item)

    def remove_item(self, item_id: str) -> Item | None:
        if self.status != OrderStatus.CREATING:
            raise ValueError(f"Cannot remove item. Your order is currently {self.status}")
        self.items = [item for item in self.items
                        if item.item_id != item_id]

    def get_item(self, item_id: str) -> Item | None:
        return next((item for item in self.items
                        if item.item_id == item_id), None)

    def order_total(self) -> float:
        return sum(item.total_price() for item in self.items)

    def update_status(self, new_status: OrderStatus):
        self.status = new_status
        
        if self._notification_service:
            self._notification_service.notify_user_of_order_status(
                customer_id = self.customer_id,
                order_id = self.order_id,
                new_status = new_status.value,
            )

    def start_order(self):
        if self.items == []:
            raise ValueError("Cannot start your order with no items.")
        if not self.status.can_start():
            raise ValueError(f"Cannot start your order. Your order is currently {self.status}.")
        self.update_status(OrderStatus.PENDING)

    def cancel_order(self):
        if not self.status.can_cancel():
            if self.status == OrderStatus.CREATING:
                raise ValueError(f"Cannot cancel your order. Your order hasn't been started yet.")
            elif self.status == OrderStatus.DELIVERED:
                raise ValueError(f"Cannot cancel your order. Your order has already been delivered.")
            else:
                raise ValueError(f"Cannot cancel your order. Your order is currently {self.status}.")
        self.update_status(OrderStatus.CANCELLED)