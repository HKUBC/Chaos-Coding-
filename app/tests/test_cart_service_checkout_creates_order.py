from app.model.item import Item
from app.model.order_status import OrderStatus
from app.services.cart_service import CartService

def test_cart_service_checkout_creates_order():
    service = CartService()
    item = Item(item_id="i1", name="Burger", price=9.99, quantity=1)
    service.add_item("customer1", "restaurant1", item)
    order = service.checkout("customer1", "order1")
    assert order.order_id == "order1"
    assert order.customer_id == "customer1"
    assert order.restaurant_id == "restaurant1"
    assert order.status == OrderStatus.PENDING
    assert len(order.items) == 1
    assert service.get_cart("customer1") is None
