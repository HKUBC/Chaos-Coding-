from app.model.cart import Cart
from app.model.item import Item

def test_cart_add_duplicate_item_merges_quantity():
    cart = Cart("customer1", "restaurant1")
    item1 = Item(item_id="i1", name="Burger", price=9.99, quantity=1)
    item2 = Item(item_id="i1", name="Burger", price=9.99, quantity=2)
    cart.add_item(item1)
    cart.add_item(item2)
    assert len(cart.items) == 1
    assert cart.items[0].quantity == 3
