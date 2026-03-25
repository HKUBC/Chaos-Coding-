from app.model.payment import Payment
from app.model.payment_status import PaymentStatus
from app.services.notification_service import NotificationService
from app.services.card_validator import CardValidator
from app.model.order import Order
from app.model.order_status import OrderStatus

notification_service = NotificationService()

#adding all the checks for the User Story "pyaments should be done safely"


# this is the service that will process the payment and update the status of the payment object, it will also notify the restaurant that a payment has been confirmed for their order
class PaymentService:

    #created a list to keep track of the orders that have been paid for
    def __init__(self):
        self._paid_orders = set()

    def process_payment(self, payment: Payment, order: Order) -> Payment:

        # 1 check - this only allows payments for the orders that are still pending
        # only pending orders can be paid for.
        if order.status != OrderStatus.PENDING:
            raise ValueError(f"Cannot process payment. Order is currently {order.status}.")

        # 2nd check - the payment amount must be same as the order total amount
        if payment.amount != (order.order_total() * payment.total_taxes) + payment.delivery_fee:
            raise ValueError(
                f"Payment amount ${payment.amount} does not match order total ${(order.order_total() * payment.total_taxes) + payment.delivery_fee}."
            )

        # 3rd check: prevent paying for the same order twice
        # this checks if the order is in the paid list and if it is, it raises and error.
        if order.order_id in self._paid_orders:
            raise ValueError(f"Order {order.order_id} has already been paid.")

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
            self._paid_orders.add(order.order_id)  # mark this order as paid
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

    # this is the function that will release the order to the restaurant for preparation, it will check if the payment has been approved before releasing the order to the restaurant
    def release_order_to_restaurant(self, order: Order):
        # check for business owner that the payment from the customer was sucessfully approved before sending the order to the restaurant for preparation

        if order.order_id not in self._paid_orders:
            raise ValueError(f"Order {order.order_id} cannot be prepared — payment has not been completed.")
        order.update_status(OrderStatus.PREPARING)
