from app.model.payment import Payment
from app.model.payment_status import PaymentStatus
from app.model.order import Order
from app.model.item import Item
from app.services.payment_service import PaymentService


def test_payment_amount_matches_order():
    order = Order(order_id="o1", customer_id="c1", restaurant_id="r1")
    order.add_item(Item(item_id=1, name="Burger", price=25.00))
    order.start_order()  # moves order to PENDING

    payment = Payment(payment_id="p1", order_id="o1", amount=(25.00 * 1.12) + 2.50, method="paypal")

    service = PaymentService()
    result = service.process_payment(payment, order)

    assert result.status == PaymentStatus.APPROVED
