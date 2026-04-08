from app.model.cart import Cart
from app.model.item import Item
from app.model.order import Order


class CartService:
    """
    Manages per-customer carts in memory.
    """

    def __init__(self):
        self._carts: dict[str, Cart] = {}  # keyed by customer_id

    def get_cart(self, customer_id: str) -> Cart | None:
        return self._carts.get(customer_id)

    def add_item(self, customer_id: str, restaurant_id: str, item: Item) -> Cart:
        cart = self._carts.get(customer_id)
        if cart is None:
            cart = Cart(customer_id, restaurant_id)
            self._carts[customer_id] = cart
        elif cart.restaurant_id != restaurant_id:
            raise ValueError(
                f"Your cart already has items from restaurant {cart.restaurant_id}. "
                "Clear the cart before adding items from a different restaurant."
            )
        cart.add_item(item)
        return cart

    def remove_item(self, customer_id: str, item_id: str) -> Cart:
        cart = self._carts.get(customer_id)
        if cart is None:
            raise ValueError("Cart is empty.")
        cart.remove_item(item_id)
        return cart

    def update_quantity(self, customer_id: str, item_id: str, quantity: int) -> Cart:
        cart = self._carts.get(customer_id)
        if cart is None:
            raise ValueError("Cart is empty.")
        cart.update_quantity(item_id, quantity)
        return cart

    def clear_cart(self, customer_id: str) -> None:
        if customer_id in self._carts:
            del self._carts[customer_id]

    def checkout(self, customer_id: str, order_id: str) -> Order:
        cart = self._carts.get(customer_id)
        if cart is None or not cart.items:
            raise ValueError("Cannot checkout with an empty cart.")

        order = Order(order_id, customer_id, cart.restaurant_id)
        for item in cart.items:
            order.add_item(item)
        order.start_order()

        del self._carts[customer_id]
        return order
