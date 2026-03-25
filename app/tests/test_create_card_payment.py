from app.model.payment import Payment
from app.model.payment_status import PaymentStatus


def test_create_card_payment():
    payment = Payment(
        payment_id="p1",
        order_id="o1",
        amount=25.00,
        method="card",
        card_number="4111111111111111",
        expiry="12/27",
        cvv="123"
    )

    assert payment.method == "card"
    assert payment.amount == 25.00
    assert payment.status == PaymentStatus.PENDING
