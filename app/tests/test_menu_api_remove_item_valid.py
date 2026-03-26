from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_remove_existing_item():
    client.post("/menu/1/items", json={
        "item_id": "item_to_remove",
        "name": "Temp Item",
        "price": 5.00,
        "quantity": 1
    })
    response = client.delete("/menu/1/items/item_to_remove")
    assert response.status_code == 200
    assert response.json() == {"message": "Item item_to_remove removed from menu"}
