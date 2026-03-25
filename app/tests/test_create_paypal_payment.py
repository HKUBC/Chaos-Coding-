from app.model.payment import Payment
from app.model.payment_status import PaymentStatus


def test_create_paypal_payment():
    payment = Payment(
        payment_id="p3",
        order_id="o1",
        amount=42.00,
        method="paypal"
    )

    assert payment.method == "paypal"
    assert payment.status == PaymentStatus.PENDING
    assert payment.card_number is None
