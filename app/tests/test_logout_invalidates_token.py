from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_logout_invalidates_token():
    client.post("/auth/signup", json={"user_id": "user2", "password": "pass123"})
    login_response = client.post("/auth/login", json={"user_id": "user2", "password": "pass123"})
    token = login_response.json()["token"]
    client.post("/auth/logout", json={"token": token})
    response = client.post("/auth/validate", json={"token": token})
    assert response.status_code == 401