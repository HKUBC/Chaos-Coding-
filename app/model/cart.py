from app.model.item import Item


class Cart:
    """
    Stores items for a customer before they place an order.
    """

    def __init__(self, customer_id: str, restaurant_id: str):
        self.customer_id = customer_id
        self.restaurant_id = restaurant_id
        self.items: list[Item] = []

    def add_item(self, item: Item) -> None:
        existing = self.get_item(item.item_id)
        if existing:
            existing.quantity += item.quantity
        else:
            self.items.append(item)

    def remove_item(self, item_id: str) -> None:
        if not any(i.item_id == item_id for i in self.items):
            raise ValueError(f"Item {item_id} not found in cart.")
        self.items = [i for i in self.items if i.item_id != item_id]

    def get_item(self, item_id: str) -> Item | None:
        return next((i for i in self.items if i.item_id == item_id), None)

    def cart_total(self) -> float:
        return sum(i.total_price() for i in self.items)

    def update_quantity(self, item_id: str, quantity: int) -> None:
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        item = self.get_item(item_id)
        if item is None:
            raise ValueError(f"Item {item_id} not found in cart.")
        if quantity == 0:
            self.remove_item(item_id)
        else:
            item.quantity = quantity

    def clear(self) -> None:
        self.items = []
