from app.model.cart import Cart
from app.model.item import Item

def test_cart_total():
    cart = Cart("customer1", "restaurant1")
    cart.add_item(Item(item_id="i1", name="Burger", price=5.00, quantity=2))
    cart.add_item(Item(item_id="i2", name="Fries", price=3.00, quantity=1))
    assert cart.cart_total() == 13.00
