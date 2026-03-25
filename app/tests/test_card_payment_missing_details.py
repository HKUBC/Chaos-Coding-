import pytest
from app.model.payment import Payment


def test_card_payment_missing_details():
    with pytest.raises(ValueError):
        Payment(
            payment_id="p5",
            order_id="o1",
            amount=10.00,
            method="card"
            # card_number, expiry, cvv intentionally missing
        )
