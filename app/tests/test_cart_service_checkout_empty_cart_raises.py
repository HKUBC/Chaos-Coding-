from app.services.cart_service import CartService
import pytest

def test_cart_service_checkout_empty_cart_raises():
    service = CartService()
    with pytest.raises(ValueError):
        service.checkout("customer1", "order1")
