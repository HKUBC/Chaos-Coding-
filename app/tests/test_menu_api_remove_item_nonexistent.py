from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_remove_nonexistent_item():
    response = client.delete("/menu/1/items/nonexistent_id")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}
