from app.model.item import Item
from app.services.cart_service import CartService
import pytest

def test_cart_service_add_item_different_restaurant_raises():
    service = CartService()
    item1 = Item(item_id="i1", name="Burger", price=9.99, quantity=1)
    item2 = Item(item_id="i2", name="Sushi", price=14.99, quantity=1)
    service.add_item("customer1", "restaurant1", item1)
    with pytest.raises(ValueError):
        service.add_item("customer1", "restaurant2", item2)
