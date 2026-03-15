from fastapi.testclient import TestClient
from app.main import app
from app.services.restaurant_service import repo

client = TestClient(app)


def test_get_existing_restaurant():

    repo.df.loc[repo.df["restaurant_id"] == 1, "is_open"] = True

    response = client.get("/restaurants/1")

    assert response.status_code == 200


def test_get_non_existing_restaurant():

    response = client.get("/restaurants/999999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Restaurant not found"


def test_closed_restaurant_api_returns_404():

    original_value = repo.df.loc[repo.df["restaurant_id"] == 1, "is_open"].iloc[0]

    repo.df.loc[repo.df["restaurant_id"] == 1, "is_open"] = False

    response = client.get("/restaurants/1")

    assert response.status_code == 404

    repo.df.loc[repo.df["restaurant_id"] == 1, "is_open"] = original_value