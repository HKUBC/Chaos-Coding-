import pytest
from app.services.card_validator import CardValidator


def test_expired_card():
    validator = CardValidator()
    with pytest.raises(ValueError):
        validator.validate(card_number="4111111111111111", expiry="01/20", cvv="123")  # expired in 2020
