from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_logout_route_success():
    client.post("/auth/signup", json={"user_id": "user1", "password": "pass123"})
    login_response = client.post("/auth/login", json={"user_id": "user1", "password": "pass123"})
    token = login_response.json()["token"]
    response = client.post("/auth/logout", json={"token": token})
    assert response.status_code == 200