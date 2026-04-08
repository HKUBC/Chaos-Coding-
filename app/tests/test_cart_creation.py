from app.model.cart import Cart

def test_cart_creation():
    cart = Cart("customer1", "restaurant1")
    assert cart.customer_id == "customer1"
    assert cart.restaurant_id == "restaurant1"
    assert cart.items == []
