from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_cart_api_view_cart_with_items():
    client.post("/cart/customer_view_items/add", json={
        "item_id": "i1",
        "name": "Fries",
        "price": 3.50,
        "quantity": 2,
        "restaurant_id": "restaurant1"
    })
    response = client.get("/cart/customer_view_items")
    assert response.status_code == 200
    data = response.json()
    assert len(data["items"]) == 1
    assert data["total"] == 7.00
