from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_cart_api_remove_nonexistent_item():
    response = client.delete("/cart/customer_remove_missing/remove/no_such_item")
    assert response.status_code == 400
