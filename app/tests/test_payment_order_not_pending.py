import pytest
from app.model.payment import Payment
from app.model.order import Order
from app.model.item import Item
from app.services.payment_service import PaymentService


def test_payment_order_not_pending():
    order = Order(order_id="o1", customer_id="c1", restaurant_id="r1")
    order.add_item(Item(item_id=1, name="Burger", price=25.00))
    # intentionally NOT calling start_order() — order stays in CREATING

    payment = Payment(payment_id="p1", order_id="o1", amount=25.00, method="paypal")

    service = PaymentService()
    with pytest.raises(ValueError):
        service.process_payment(payment, order)
