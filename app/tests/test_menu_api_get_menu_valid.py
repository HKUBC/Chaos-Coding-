from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_menu_valid_restaurant():
    response = client.get("/menu/1")
    assert response.status_code == 200
    data = response.json()
    assert data["restaurant_id"] == 1
    assert isinstance(data["items"], list)
    assert len(data["items"]) > 0
