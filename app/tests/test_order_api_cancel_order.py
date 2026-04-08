from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from app.main import app

client = TestClient(app)

def test_api_cancel_order_valid():
    mock_order = MagicMock()

    with patch("app.services.order_service.OrderService.get_order", return_value=mock_order):
        response = client.patch("/orders/123/cancel")

    assert response.status_code == 200
    assert "cancelled successfully" in response.json()["message"]

def test_api_cancel_order_not_found():
    with patch("app.services.order_service.OrderService.get_order", return_value=None):
        response = client.patch("/orders/999/cancel")

    assert response.status_code == 404
    assert response.json()["detail"] == "Order not found"

def test_api_cancel_order_invalid_state():
    mock_order = MagicMock()

    with patch("app.services.order_service.OrderService.get_order", return_value=mock_order), \
         patch.object(mock_order, "cancel_order", side_effect=ValueError("Cannot cancel your order")):
        response = client.patch("/orders/123/cancel")

    assert response.status_code == 400
    assert "Cannot cancel your order" in response.json()["detail"]