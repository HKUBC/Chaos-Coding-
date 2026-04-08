from app.model.item import Item
from app.services.cart_service import CartService

def test_cart_service_add_item_creates_cart():
    service = CartService()
    item = Item(item_id="i1", name="Burger", price=9.99, quantity=1)
    cart = service.add_item("customer1", "restaurant1", item)
    assert cart is not None
    assert len(cart.items) == 1
    assert cart.restaurant_id == "restaurant1"
