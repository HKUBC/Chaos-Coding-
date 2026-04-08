from app.model.cart import Cart
from app.model.item import Item
import pytest

def test_cart_update_quantity_negative_raises():
    cart = Cart("customer1", "restaurant1")
    cart.add_item(Item(item_id="i1", name="Burger", price=9.99, quantity=1))
    with pytest.raises(ValueError):
        cart.update_quantity("i1", -1)
