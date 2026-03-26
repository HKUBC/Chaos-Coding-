from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_menu_invalid_restaurant():
    response = client.get("/menu/99999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Restaurant not found"}
