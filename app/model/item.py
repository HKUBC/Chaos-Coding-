class Item:
    """
    Represents an item from a menu.
    """

    def __init__(self, item_id: str, name: str, price: float, description: str = "", quantity: int = 1):
        self.item_id     = item_id
        self.name        = name
        self.price       = price
        self.description = description
        self.quantity    = quantity

    def total_price(self) -> float:
        return self.price * self.quantity
    
    def update(self, name: str = None, price: float = None, description: str = None, quantity: int = None):
        if name        is not None: self.name        = name
        if price       is not None: self.price       = price
        if description is not None: self.description = description
        if quantity    is not None: self.quantity    = quantity

    def __repr__(self) -> str:
        return f"Item(item_id='{self.item_id}', name='{self.name}', price={self.price}, quantity={self.quantity})"