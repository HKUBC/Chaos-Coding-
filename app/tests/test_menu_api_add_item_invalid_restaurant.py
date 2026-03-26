from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add_item_to_invalid_restaurant():
    response = client.post("/menu/99999/items", json={
        "item_id": "test_item_002",
        "name": "Test Pizza",
        "price": 12.99,
        "quantity": 1
    })
    assert response.status_code == 404
    assert response.json() == {"detail": "Restaurant not found"}
