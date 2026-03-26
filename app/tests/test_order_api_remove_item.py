from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from app.main import app

client = TestClient(app)

def test_api_remove_item_valid():
    mock_order = MagicMock()
    mock_order.remove_item.return_value = None

    with patch("app.services.order_service.OrderService.get_order", return_value=mock_order):
        response = client.delete("/orders/123/remove_item/1")

    assert response.status_code == 200
    assert "removed" in response.json()["message"]

def test_api_remove_item_invalid_order():
    with patch("app.services.order_service.OrderService.get_order", return_value=None):
        response = client.delete("/orders/999/remove_item/1")

    assert response.status_code == 404
    assert response.json()["detail"] == "Order not found"