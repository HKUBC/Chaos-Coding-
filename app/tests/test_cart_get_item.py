from app.model.cart import Cart
from app.model.item import Item

def test_cart_get_item():
    cart = Cart("customer1", "restaurant1")
    item = Item(item_id="i1", name="Pizza", price=12.50, quantity=1)
    cart.add_item(item)
    result = cart.get_item("i1")
    assert result is not None
    assert result.name == "Pizza"
