import pytest
from app.services.card_validator import CardValidator


def test_invalid_expiry_format():
    validator = CardValidator()
    with pytest.raises(ValueError):
        validator.validate(card_number="4111111111111111", expiry="2027/12", cvv="123")  # wrong format
