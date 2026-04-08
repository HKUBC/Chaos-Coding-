from app.model.cart import Cart
from app.model.item import Item

def test_cart_clear():
    cart = Cart("customer1", "restaurant1")
    cart.add_item(Item(item_id="i1", name="Burger", price=9.99, quantity=1))
    cart.add_item(Item(item_id="i2", name="Fries", price=3.99, quantity=2))
    cart.clear()
    assert cart.items == []
