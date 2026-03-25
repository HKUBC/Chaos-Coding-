import pytest
from app.model.order import Order
from app.model.item import Item
from app.services.payment_service import PaymentService


def test_order_cannot_prepare_without_payment():
    order = Order(order_id="o1", customer_id="c1", restaurant_id="r1")
    order.add_item(Item(item_id=1, name="Burger", price=25.00))
    order.start_order()  # moves to PENDING — but no payment made

    service = PaymentService()
    with pytest.raises(ValueError):
        service.release_order_to_restaurant(order)  # should fail — payment not completed
