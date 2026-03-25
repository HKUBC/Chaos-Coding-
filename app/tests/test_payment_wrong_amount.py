import pytest
from app.model.payment import Payment
from app.model.order import Order
from app.model.item import Item
from app.services.data_service import DataService
from app.services.payment_service import PaymentService


class FakeDataService(DataService):
    def load_data(self) -> list[dict]:
        return []


def test_payment_wrong_amount():
    order = Order(order_id="o1", customer_id="c1", restaurant_id="r1", data_service=FakeDataService())
    order.add_item(Item(item_id=1, name="Burger", price=25.00))
    order.start_order()  # moves order to PENDING

    payment = Payment(payment_id="p1", order_id="o1", amount=10.00, method="paypal")  # wrong amount

    service = PaymentService()
    with pytest.raises(ValueError):
        service.process_payment(payment, order)
