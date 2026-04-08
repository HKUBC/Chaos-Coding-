from uuid import uuid4
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.model.payment import Payment
from app.services.payment_service import PaymentService
from app.services.order_service import OrderService

router = APIRouter(prefix="/payments", tags=["Payments"])

payment_service = PaymentService()
order_service = OrderService()

class PaymentRequest(BaseModel):
    method: str
    card_number: str | None = None
    expiry: str | None = None
    cvv: str | None = None

@router.post("/{order_id}/pay")
def pay_for_order(order_id: str, request: PaymentRequest):
    order = order_service.get_order(order_id)

    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")

    # backend is SINGLE source of truth
    subtotal = order.order_total()
    taxes = subtotal * 0.12
    delivery_fee = 2.50
    total = subtotal + taxes + delivery_fee

    payment = Payment(
        payment_id=str(uuid4()),
        order_id=order.order_id,
        amount=total,
        method=request.method,
        customer_id=order.customer_id,
        restaurant_id=order.restaurant_id,
        card_number=request.card_number,
        expiry=request.expiry,
        cvv=request.cvv,
    )

    try:
        payment = payment_service.process_payment(payment, order)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    if payment.status.value == "approved":
        payment_service.release_order_to_restaurant(order)

    return {
        "order_id": order_id,
        "total": total,
        "status": payment.status.value,
        "order_status": order.status.value
    }