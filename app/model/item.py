class Item:
    """
    Represents an item from a menu.
    """

    def __init__(self, item_id: int, name: str, price: float, quantity: int = 1):

        if price < 0: # test to check if the price is negative, if it is then raise a ValueError
            raise ValueError("Price cannot be negative.")
        
        

        self.item_id = item_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self) -> float:
        return self.price * self.quantity
    
    def update(self, name: int = None, price: float = None, description: str = None, quantity: int = None): # pyright: ignore[reportArgumentType]
        if name        is not None: self.name        = name
        if price       is not None: self.price       = price
        if quantity    is not None: self.quantity    = quantity

    def __repr__(self) -> str:
        return f"Item(item_id='{self.item_id}', name='{self.name}', price={self.price}, quantity={self.quantity})"