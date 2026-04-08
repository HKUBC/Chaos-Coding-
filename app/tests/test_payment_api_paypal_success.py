from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_payment_api_paypal_success():
    # Add item and checkout to get a PENDING order
    client.post("/cart/customer_pay_paypal/add", json={
        "item_id": "i1",
        "name": "Burger",
        "price": 10.00,
        "quantity": 1,
        "restaurant_id": "restaurant1"
    })
    checkout = client.post("/cart/customer_pay_paypal/checkout")
    order_id = checkout.json()["order_id"]

    # Use the same float arithmetic the service uses to avoid precision mismatch
    amount = (10.00 * 1.12) + 2.50  # order_total * taxes + delivery_fee
    response = client.post(f"/payment/{order_id}", json={
        "customer_id": "customer_pay_paypal",
        "restaurant_id": "restaurant1",
        "amount": amount,
        "method": "paypal"
    })
    assert response.status_code == 200
    assert response.json()["status"] == "approved"
