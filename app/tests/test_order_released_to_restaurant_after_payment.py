from app.model.payment import Payment
from app.model.order import Order
from app.model.item import Item
from app.model.order_status import OrderStatus
from app.services.payment_service import PaymentService


def test_order_released_to_restaurant_after_payment():
    order = Order(order_id="o1", customer_id="c1", restaurant_id="r1")
    order.add_item(Item(item_id=1, name="Burger", price=25.00))
    order.start_order()  # moves to PENDING

    payment = Payment(payment_id="p1", order_id="o1", amount=25.00, method="paypal")

    service = PaymentService()
    service.process_payment(payment, order)       # payment approved
    service.release_order_to_restaurant(order)    # should move order to PREPARING

    assert order.status == OrderStatus.PREPARING
