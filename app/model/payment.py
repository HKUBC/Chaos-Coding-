from app.model.payment_status import PaymentStatus

##options to pay for the order
VALID_METHODS = {"card", "apple_pay", "paypal"}

class Payment:
   
    # all the values required to create a payment object, the card details are optional and only required if the payment method is card
    def __init__(self, payment_id: str, order_id: str, amount: float, method: str,
                 card_number: str | None = None, expiry: str | None = None, cvv: str | None = None):

        # to check the method choosed is valid or not
        if method not in VALID_METHODS:
            raise ValueError(f"Invalid payment method '{method}'. Choose from: {VALID_METHODS}")

        #to check the amount is not negative or zero
        if amount <= 0:
            raise ValueError("Payment amount must be greater than 0.")
       
        # to check if all the card details are provided
        if method == "card":
            if not card_number or not expiry or not cvv:
                raise ValueError("Card payments require card_number, expiry, and cvv.")

        self.payment_id  = payment_id
        self.order_id    = order_id
        self.amount      = amount
        self.method      = method
        self.card_number = card_number  # stored as-is for simulation; mask in production
        self.expiry      = expiry
        self.cvv         = cvv
        self.status      = PaymentStatus.PENDING

#this is just giving out the details of the payment object
    def display(self):
        return (f"Payment(payment_id='{self.payment_id}', order_id='{self.order_id}', "
                f"amount={self.amount}, method='{self.method}', status={self.status})")
