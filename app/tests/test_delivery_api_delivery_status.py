from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from app.main import app

client = TestClient(app)

def test_api_delivery_status_with_valid_order():
    mock_order = MagicMock()
    mock_order.order_id = "1d8e87M"
    mock_order.status.can_deliver.return_value = True

    with patch("app.api.routes.delivery_route.order_service") as mock_order_service, \
         patch("app.services.delivery_service.DeliveryRepository") as mock_repo:
        mock_repo.return_value.deliveries = {}
        mock_order_service.get_order.return_value = mock_order

        client.post("/deliveries/1d8e87M/assign")
        response = client.get("/deliveries/1d8e87M/delivery_status")

        assert response.status_code == 200

def test_api_delivery_status_with_invalid_order():
    response = client.get("/deliveries/invalid_order_id/delivery_status")

    assert response.status_code == 404
    assert response.json() == {"detail": "Delivery not found"}