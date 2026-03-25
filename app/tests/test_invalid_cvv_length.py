import pytest
from app.services.card_validator import CardValidator


def test_invalid_cvv_length():
    validator = CardValidator()
    with pytest.raises(ValueError):
        validator.validate(card_number="4111111111111111", expiry="12/27", cvv="12")  # only 2 digits
