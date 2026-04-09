from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from app.main import app

client = TestClient(app)

def test_api_assign_delivery_to_valid_order():
    mock_order = MagicMock()
    mock_order.order_id = "1d8e87M"
    mock_order.status.can_deliver.return_value = True

    with patch("app.api.routes.delivery_route.order_service") as mock_order_service:
        mock_order_service.get_order.return_value = mock_order

        response = client.post("/deliveries/1d8e87M/assign")

        assert response.status_code == 200

def test_api_assign_delivery_to_invalid_order():
    with patch("app.api.routes.delivery_route.order_service") as mock_order_service:
        mock_order_service.get_order.return_value = None

        response = client.post("/deliveries/invalid_order_id/assign")

        assert response.status_code == 404
        assert response.json() == {"detail": "Order not found"}