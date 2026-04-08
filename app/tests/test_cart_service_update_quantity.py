from app.model.item import Item
from app.services.cart_service import CartService

def test_cart_service_update_quantity():
    service = CartService()
    service.add_item("customer1", "restaurant1", Item(item_id="i1", name="Burger", price=9.99, quantity=1))
    cart = service.update_quantity("customer1", "i1", 5)
    assert cart.get_item("i1").quantity == 5
