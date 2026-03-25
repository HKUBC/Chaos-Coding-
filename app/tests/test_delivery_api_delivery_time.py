from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app
from app.services.delivery_service import repo

client = TestClient(app)

def test_api_get_delivery_time_valid_order():
    with patch("app.services.delivery_service.repo") as mock_repo:
        mock_repo.deliveries = {}

        with patch("app.services.order_service.repo") as mock_order_repo:
            mock_order_repo.get_order_by_id.return_value = {
                "order_id": "1d8e87M",
                "customer_id": "9c6dbfcb-72c5-4cc4-9f76-29200f0efda7",
                "restaurant_id": "16"
            }

            client.post("/deliveries/1d8e87M/assign")
            response = client.get("/deliveries/1d8e87M/time")
            assert response.status_code == 200

def test_api_get_delivery_time_invalid_order():
    with patch("app.services.delivery_service.repo") as mock_repo:
        mock_repo.deliveries = {}
        mock_repo.get_delivery_time.return_value = None

        response = client.get("/deliveries/invalid_order_id/time")
        assert response.status_code == 404
        assert response.json() == {"detail": "Delivery not found"}