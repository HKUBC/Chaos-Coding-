from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_cart_api_update_quantity():
    client.post("/cart/customer_update_qty/add", json={
        "item_id": "i1",
        "name": "Burger",
        "price": 9.99,
        "quantity": 1,
        "restaurant_id": "restaurant1"
    })
    response = client.patch("/cart/customer_update_qty/update/i1", json={"quantity": 4})
    assert response.status_code == 200
    data = response.json()
    assert data["cart"]["items"][0]["quantity"] == 4
