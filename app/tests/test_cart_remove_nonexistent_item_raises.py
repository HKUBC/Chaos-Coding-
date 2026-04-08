from app.model.cart import Cart
import pytest

def test_cart_remove_nonexistent_item_raises():
    cart = Cart("customer1", "restaurant1")
    with pytest.raises(ValueError):
        cart.remove_item("nonexistent_id")
