import pytest
from app.services.card_validator import CardValidator


def test_invalid_card_number_length():
    validator = CardValidator()
    with pytest.raises(ValueError):
        validator.validate(card_number="411111111111", expiry="12/27", cvv="123")  # only 12 digits
