from app.model.cart import Cart
from app.model.item import Item

def test_cart_remove_item():
    cart = Cart("customer1", "restaurant1")
    item = Item(item_id="i1", name="Burger", price=9.99, quantity=1)
    cart.add_item(item)
    cart.remove_item("i1")
    assert cart.items == []
