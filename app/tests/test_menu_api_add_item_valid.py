from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add_item_to_valid_restaurant():
    response = client.post("/menu/1/items", json={
        "item_id": "test_item_001",
        "name": "Test Burger",
        "price": 9.99,
        "quantity": 1
    })
    assert response.status_code == 200
    assert response.json() == {"message": "Item 'Test Burger' added to menu"}
