from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_cart_api_checkout_empty_cart():
    response = client.post("/cart/customer_checkout_empty/checkout")
    assert response.status_code == 400
