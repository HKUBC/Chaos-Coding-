from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_cart_api_add_item():
    response = client.post("/cart/customer_add_item/add", json={
        "item_id": "i1",
        "name": "Burger",
        "price": 9.99,
        "quantity": 1,
        "restaurant_id": "restaurant1"
    })
    assert response.status_code == 200
    data = response.json()
    assert "cart" in data
    assert len(data["cart"]["items"]) == 1
    assert data["cart"]["items"][0]["name"] == "Burger"
