from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from app.main import app

client = TestClient(app)

def test_api_delete_existing_order_promotion():
    mock_promo = MagicMock()
    mock_promo.promo_id = "p1"

    with patch("app.api.routes.promotion_route.promotion_service") as mock_promo_service:
        mock_promo_service.order_promotions = [mock_promo]
        response = client.delete("/promotions/order/p1")

    assert response.status_code == 200
    assert response.json()["message"] == "Order promotion p1 deleted successfully"

def test_api_delete_nonexistent_order_promotion():
    with patch("app.api.routes.promotion_route.promotion_service") as mock_promo_service:
        mock_promo_service.order_promotions = []
        response = client.delete("/promotions/order/p1")

    assert response.status_code == 404
    assert response.json()["detail"] == "Order promotion wasn't found"