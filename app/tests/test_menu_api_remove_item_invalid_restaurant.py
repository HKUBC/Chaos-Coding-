from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_remove_item_from_invalid_restaurant():
    response = client.delete("/menu/99999/items/ae28e9V")
    assert response.status_code == 404
    assert response.json() == {"detail": "Restaurant not found"}
