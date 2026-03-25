import pytest
from app.model.payment import Payment


def test_invalid_payment_method():
    with pytest.raises(ValueError):
        Payment(
            payment_id="p4",
            order_id="o1",
            amount=10.00,
            method="bitcoin"
        )
