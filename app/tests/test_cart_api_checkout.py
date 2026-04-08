from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_cart_api_checkout():
    client.post("/cart/customer_checkout/add", json={
        "item_id": "i1",
        "name": "Burger",
        "price": 9.99,
        "quantity": 1,
        "restaurant_id": "restaurant1"
    })
    response = client.post("/cart/customer_checkout/checkout")
    assert response.status_code == 200
    data = response.json()
    assert "order_id" in data
    assert data["status"] == "pending"
    assert len(data["items"]) == 1
