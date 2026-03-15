from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_existing_restaurant():

    response = client.get("/restaurants/1")

    assert response.status_code == 200
    assert "restaurant_id" in response.json()


def test_get_non_existing_restaurant():

    response = client.get("/restaurants/999999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Restaurant not found"