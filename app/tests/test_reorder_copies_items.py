from app.services.order_service import OrderService
from app.model.order import Order
from app.model.item import Item

def test_reorder_copies_items():
    service = OrderService()
    order = Order("o1", "cust_1", "rest_1")
    order.add_item(Item(1, "Burger", 10.0))
    service.place_order(order)
    new_order = service.reorder("cust_1", "o1", "o2")
    assert len(new_order.items) == 1
    assert new_order.items[0].name == "Burger"