from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_favorite_restaurant_api():

    response = client.post("/restaurants/1/favorite")

    assert response.status_code == 200