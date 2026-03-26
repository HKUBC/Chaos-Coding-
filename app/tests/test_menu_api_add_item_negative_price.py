from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add_item_with_negative_price():
    response = client.post("/menu/1/items", json={
        "item_id": "test_item_003",
        "name": "Bad Item",
        "price": -5.00,
        "quantity": 1
    })
    assert response.status_code == 400
