from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from app.main import app

client = TestClient(app)

def test_api_get_item_valid():
    mock_item = MagicMock()
    mock_item.item_id = "1"
    mock_item.name = "Burger"
    mock_item.price = 10.0
    mock_item.quantity = 2
    mock_item.restaurant_id = "rest1"

    mock_order = MagicMock()
    mock_order.get_item.return_value = mock_item

    with patch("app.services.order_service.OrderService.get_order", return_value=mock_order):
        response = client.get("/orders/123/items/1")

    assert response.status_code == 200
    data = response.json()
    assert data["item_id"] == "1"
    assert data["item_name"] == "Burger"

def test_api_get_item_order_not_found():
    with patch("app.services.order_service.OrderService.get_order", return_value=None):
        response = client.get("/orders/999/items/1")

    assert response.status_code == 404
    assert response.json()["detail"] == "Order not found"

def test_api_get_item_not_found():
    mock_order = MagicMock()
    mock_order.get_item.return_value = None

    with patch("app.services.order_service.OrderService.get_order", return_value=mock_order):
        response = client.get("/orders/123/items/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"