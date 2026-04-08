from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_cart_api_remove_item():
    client.post("/cart/customer_remove/add", json={
        "item_id": "i1",
        "name": "Burger",
        "price": 9.99,
        "quantity": 1,
        "restaurant_id": "restaurant1"
    })
    response = client.delete("/cart/customer_remove/remove/i1")
    assert response.status_code == 200
    data = response.json()
    assert data["cart"]["items"] == []
