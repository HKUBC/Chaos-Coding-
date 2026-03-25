from app.services.order_service import OrderService
from app.model.order import Order
from app.model.item import Item

def test_order_history_returns_correct_customer():
    service = OrderService()
    order = Order("o1", "cust_1", "rest_1")
    order.add_item(Item(1, "Burger", 10.0))
    service.place_order(order)
    assert service.get_order_history("cust_2") == []