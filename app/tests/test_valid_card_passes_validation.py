from app.services.card_validator import CardValidator


def test_valid_card_passes_validation():
    validator = CardValidator()
    # should not raise any exception
    validator.validate(card_number="4111111111111111", expiry="12/27", cvv="123")
