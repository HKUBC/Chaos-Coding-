from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_payment_api_invalid_method():
    client.post("/cart/customer_pay_invalid/add", json={
        "item_id": "i1",
        "name": "Burger",
        "price": 10.00,
        "quantity": 1,
        "restaurant_id": "restaurant1"
    })
    checkout = client.post("/cart/customer_pay_invalid/checkout")
    order_id = checkout.json()["order_id"]

    response = client.post(f"/payment/{order_id}", json={
        "customer_id": "customer_pay_invalid",
        "restaurant_id": "restaurant1",
        "amount": 13.70,
        "method": "bitcoin"
    })
    assert response.status_code == 400
