from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_logout_invalid_token_raises():
    response = client.post("/auth/logout", json={"token": "fake_token"})
    assert response.status_code == 401