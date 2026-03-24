from app.model.payment import Payment
from app.model.payment_status import PaymentStatus
from app.services.notification_service import NotificationService

notification_service = NotificationService()


class PaymentService:
    """
    Simulates payment processing.
    Accepts a Payment object and sets its status to APPROVED or DECLINED.
    No real payment gateway is connected — this is a simulation.
    """

    def process_payment(self, payment: Payment) -> Payment:
        """
        Process the payment and update its status.
        For card payments, validation is handled separately (sub-issue 2).
        All non-card methods (apple_pay, paypal) are approved immediately.
        """
        payment.status = PaymentStatus.APPROVED
        return payment
