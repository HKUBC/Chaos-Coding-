from app.services.order_service import OrderService
from app.model.order import Order
from app.model.item import Item

def test_order_history_contains_order_id():
    service = OrderService()
    order = Order("o1", "cust_1", "rest_1")
    order.add_item(Item(1, "Burger", 10.0))
    service.place_order(order)
    history = service.get_order_history("cust_1")
    assert history[0]["order_id"] == "o1"