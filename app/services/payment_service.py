from app.model.payment import Payment
from app.model.payment_status import PaymentStatus
from app.services.notification_service import NotificationService
from app.services.card_validator import CardValidator

notification_service = NotificationService()

# this is the service that will process the payment and update the status of the payment object, it will also notify the restaurant that a payment has been confirmed for their order
class PaymentService:

    def process_payment(self, payment: Payment) -> Payment:

        approved = True
        # created method for only card payments
        # validate card details before approving
        if payment.method == "card":
            try:
                CardValidator().validate(payment.card_number, payment.expiry, payment.cvv)
            except ValueError:
                approved = False
# if the card details are valid, we can approve the payment, otherwise we will decline it
        if approved:
            payment.status = PaymentStatus.APPROVED # this changes the status to approved
        else:
            payment.status = PaymentStatus.DECLINED


        # notify the restaurant that a payment has been confirmed for their order
        if payment.restaurant_id and payment.customer_id:
            notification_service.notify_restaurant_of_order(
                restaurant_id=payment.restaurant_id,
                order_id=payment.order_id,
                customer_id=payment.customer_id,
                order_total=payment.amount,
            )
    
       
        if payment.customer_id:
            notification_service.notify_user_of_payment(
                customer_id=payment.customer_id,
                order_id=payment.order_id,
                amount=payment.amount,
                approved=approved,
            )

        return payment

