from app.model.payment import Payment
from app.model.payment_status import PaymentStatus


def test_create_apple_pay_payment():
    payment = Payment(
        payment_id="p2",
        order_id="o1",
        amount=15.50,
        method="apple_pay"
    )

    assert payment.method == "apple_pay"
    assert payment.status == PaymentStatus.PENDING
    assert payment.card_number is None
