from app.model.cart import Cart
from app.model.item import Item

def test_cart_update_quantity():
    cart = Cart("customer1", "restaurant1")
    cart.add_item(Item(item_id="i1", name="Burger", price=9.99, quantity=1))
    cart.update_quantity("i1", 3)
    assert cart.get_item("i1").quantity == 3
