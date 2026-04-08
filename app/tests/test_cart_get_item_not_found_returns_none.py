from app.model.cart import Cart

def test_cart_get_item_not_found_returns_none():
    cart = Cart("customer1", "restaurant1")
    result = cart.get_item("does_not_exist")
    assert result is None
