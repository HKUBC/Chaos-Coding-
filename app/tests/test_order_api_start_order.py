from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from app.main import app

client = TestClient(app)

def test_api_start_order_valid():
    mock_order = MagicMock()
    mock_order.start_order.return_value = None

    with patch("app.services.order_service.OrderService.get_order", return_value=mock_order):
        response = client.post("/orders/123/start")

    assert response.status_code == 200
    assert "started successfully" in response.json()["message"]

def test_api_start_order_not_found():
    with patch("app.services.order_service.OrderService.get_order", return_value=None):
        response = client.post("/orders/999/start")

    assert response.status_code == 404
    assert response.json()["detail"] == "Order not found"

def test_api_start_order_invalid_state():
    mock_order = MagicMock()
    mock_order.start_order.side_effect = ValueError("Cannot start your order")

    with patch("app.services.order_service.OrderService.get_order", return_value=mock_order):
        response = client.post("/orders/123/start")

    assert response.status_code == 400
    assert "Cannot start your order" in response.json()["detail"]