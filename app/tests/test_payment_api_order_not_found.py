from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_payment_api_order_not_found():
    response = client.post("/payment/nonexistent_order_id", json={
        "customer_id": "customer1",
        "restaurant_id": "restaurant1",
        "amount": 13.70,
        "method": "paypal"
    })
    assert response.status_code == 404
