from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.model.payment import Payment
from app.services.payment_service import PaymentService
from app.services.order_service import repo as order_repo  # shared singleton
import uuid

router = APIRouter(prefix="/payment", tags=["Payment"])

payment_service = PaymentService()


class PaymentRequest(BaseModel):
    customer_id: str
    restaurant_id: str
    amount: float
    method: str                   # "card", "apple_pay", or "paypal"
    card_number: str | None = None
    expiry: str | None = None
    cvv: str | None = None


@router.post("/{order_id}")
def process_payment(order_id: str, request: PaymentRequest):
    # Retrieve the session order so we have the Order object (not CSV DataFrame)
    session_orders = order_repo.get_session_orders(request.customer_id)
    order = next((o for o in session_orders if o.order_id == order_id), None)

    if order is None:
        raise HTTPException(status_code=404, detail="Order not found.")

    try:
        payment = Payment(
            payment_id=str(uuid.uuid4()),
            order_id=order_id,
            amount=request.amount,
            method=request.method,
            customer_id=request.customer_id,
            restaurant_id=request.restaurant_id,
            card_number=request.card_number,
            expiry=request.expiry,
            cvv=request.cvv,
        )
        result = payment_service.process_payment(payment, order)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {
        "payment_id": result.payment_id,
        "order_id": result.order_id,
        "amount": result.amount,
        "method": result.method,
        "status": result.status.value,
    }
