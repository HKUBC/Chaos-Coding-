from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_cart_api_add_invalid_item():
    response = client.post("/cart/customer_add_invalid/add", json={
        "item_id": "i1",
        "name": "Bad Item",
        "price": -5.00,
        "quantity": 1,
        "restaurant_id": "restaurant1"
    })
    assert response.status_code == 400
