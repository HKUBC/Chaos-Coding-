import pytest
from app.services.card_validator import CardValidator


def test_card_number_not_digits():
    validator = CardValidator()
    with pytest.raises(ValueError):
        validator.validate(card_number="41111111111111AB", expiry="12/27", cvv="123")  # letters in card
