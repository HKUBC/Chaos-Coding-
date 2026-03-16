from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)




def test_remove_favorite_api():

    client.post("/restaurants/1/favorite")

    response = client.delete("/restaurants/1/favorite")

    assert response.status_code == 200