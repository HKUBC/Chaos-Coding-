from app.model.item import Item
from app.services.cart_service import CartService

def test_cart_service_remove_item():
    service = CartService()
    item = Item(item_id="i1", name="Burger", price=9.99, quantity=1)
    service.add_item("customer1", "restaurant1", item)
    cart = service.remove_item("customer1", "i1")
    assert cart.items == []
