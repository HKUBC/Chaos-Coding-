from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_cart_api_view_empty_cart():
    response = client.get("/cart/customer_view_empty")
    assert response.status_code == 200
    data = response.json()
    assert data["items"] == []
    assert data["total"] == 0.0
