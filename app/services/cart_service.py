import json
import os

from app.model.cart import Cart
from app.model.item import Item
from app.model.order import Order

_DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'carts.json')


class CartService:
    """
    Manages per-customer carts in memory, persisted to disk so data survives server restarts.
    """

    def __init__(self):
        self._carts: dict[str, Cart] = {}
        self._load()

    def _load(self):
        if not os.path.exists(_DATA_FILE):
            return
        try:
            with open(_DATA_FILE, 'r') as f:
                data = json.load(f)
            for customer_id, cart_data in data.items():
                cart = Cart(customer_id, cart_data['restaurant_id'])
                for item_data in cart_data['items']:
                    item = Item(
                        item_id=item_data['item_id'],
                        name=item_data['name'],
                        price=item_data['price'],
                        quantity=item_data['quantity'],
                    )
                    cart.items.append(item)
                self._carts[customer_id] = cart
        except Exception:
            pass

    def _save(self):
        data = {}
        for customer_id, cart in self._carts.items():
            data[customer_id] = {
                'restaurant_id': cart.restaurant_id,
                'items': [
                    {
                        'item_id': i.item_id,
                        'name': i.name,
                        'price': i.price,
                        'quantity': i.quantity,
                    }
                    for i in cart.items
                ],
            }
        with open(_DATA_FILE, 'w') as f:
            json.dump(data, f, indent=2)  # keyed by customer_id

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
        self._save()
        return cart

    def remove_item(self, customer_id: str, item_id: str) -> Cart:
        cart = self._carts.get(customer_id)
        if cart is None:
            raise ValueError("Cart is empty.")
        cart.remove_item(item_id)
        self._save()
        return cart

    def update_quantity(self, customer_id: str, item_id: str, quantity: int) -> Cart:
        cart = self._carts.get(customer_id)
        if cart is None:
            raise ValueError("Cart is empty.")
        cart.update_quantity(item_id, quantity)
        self._save()
        return cart

    def clear_cart(self, customer_id: str) -> None:
        if customer_id in self._carts:
            del self._carts[customer_id]
            self._save()

    def checkout(self, customer_id: str, order_id: str) -> Order:
        cart = self._carts.get(customer_id)
        if cart is None or not cart.items:
            raise ValueError("Cannot checkout with an empty cart.")

        order = Order(order_id, customer_id, cart.restaurant_id)
        for item in cart.items:
            order.add_item(item)
        order.start_order()

        del self._carts[customer_id]
        self._save()
        return order
