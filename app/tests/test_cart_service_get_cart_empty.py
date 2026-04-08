from app.services.cart_service import CartService

def test_cart_service_get_cart_empty():
    service = CartService()
    result = service.get_cart("customer1")
    assert result is None
