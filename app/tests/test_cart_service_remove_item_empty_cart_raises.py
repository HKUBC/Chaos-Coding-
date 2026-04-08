from app.services.cart_service import CartService
import pytest

def test_cart_service_remove_item_empty_cart_raises():
    service = CartService()
    with pytest.raises(ValueError):
        service.remove_item("customer1", "i1")
