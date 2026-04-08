from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_cart_api_clear_cart():
    client.post("/cart/customer_clear/add", json={
        "item_id": "i1",
        "name": "Burger",
        "price": 9.99,
        "quantity": 1,
        "restaurant_id": "restaurant1"
    })
    response = client.delete("/cart/customer_clear/clear")
    assert response.status_code == 200
    view = client.get("/cart/customer_clear")
    assert view.json()["items"] == []
