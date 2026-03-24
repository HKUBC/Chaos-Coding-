from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)




def test_get_favorites_api():

    client.post("/restaurants/1/favorite")

    response = client.get("/restaurants/favorites")

    assert response.status_code == 200

    assert isinstance(response.json(), list)