import pytest
from app.model.payment import Payment
from app.model.order import Order
from app.model.item import Item
from app.services.payment_service import PaymentService


def test_payment_duplicate_order():
    order = Order(order_id="o1", customer_id="c1", restaurant_id="r1")
    order.add_item(Item(item_id=1, name="Burger", price=25.00))
    order.start_order()  # moves order to PENDING

    payment1 = Payment(payment_id="p1", order_id="o1", amount=(25.00 * 1.12) + 2.50, method="paypal")
    payment2 = Payment(payment_id="p2", order_id="o1", amount=(25.00 * 1.12) + 2.50, method="paypal")

    service = PaymentService()
    service.process_payment(payment1, order)  # first payment goes through

    with pytest.raises(ValueError):
        service.process_payment(payment2, order)  # second payment on same order should fail