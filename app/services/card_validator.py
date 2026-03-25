from datetime import datetime

class CardValidator:

    def validate(self, card_number, expiry, cvv):
        # check card number is exactly 16 digits
        if len(card_number) != 16 or not card_number.isdigit():
            raise ValueError("Invalid card number. Must be 16 digits.")

        # check cvv is exactly 3 digits
        if len(cvv) != 3 or not cvv.isdigit():
            raise ValueError("Invalid CVV. Must be 3 digits.")

        # check expiry format is MM/YY
        try:
            month, year = expiry.split("/")
            expiry_date = datetime(2000 + int(year), int(month), 1)
        except Exception:
            raise ValueError("Invalid expiry format. Use MM/YY (e.g. 12/27).")

        # check card is not expired
        # the logic i used here is to set the expiry date to the first day of 
        # the month following the expiry month, and then compare it to the current date. 
        # If the expiry date is in the past, then the card is expired.
        today = datetime.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        if expiry_date < today:
            raise ValueError("Card is expired.")
