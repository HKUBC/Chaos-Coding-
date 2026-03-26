from fastapi.testclient import TestClient
from unittest.mock import MagicMock, patch
from app.main import app
from app.services.order_service import repo

client = TestClient(app)

def test_api_add_item_with_valid_order():
    mock_order = MagicMock()
    mock_order.add_item.return_value = None

    with patch("app.services.order_service.OrderService.get_order", return_value = mock_order):
        response = client.post(
            "/orders/123/add_item",
            json={
                "item_id": "1",
                "name": "Burger",
                "price": 10.0,
                "quantity": 1
            }
        )

    assert response.status_code == 200
    assert "added" in response.json()["message"]

def test_api_add_item_width_invalid_order():
    with patch("app.services.order_service.OrderService.get_order", return_value = None):
        response = client.post(
            "/orders/999/add_item",
            json={
                "item_id": "1",
                "name": "Burger",
                "price": 10.0,
                "quantity": 1
            }
        )

    assert response.status_code == 404
    assert response.json()["detail"] == "Order not found"