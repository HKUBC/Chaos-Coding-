from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from app.main import app

client = TestClient(app)

def test_api_apply_valid_order_promotion():
    mock_order = MagicMock()
    mock_order.total = 200.0

    with patch("app.api.routes.promotion_route.promotion_service") as mock_promo_service, \
         patch("app.api.routes.promotion_route.order_service") as mock_order_service:
        mock_order_service.get_order.return_value = mock_order
        mock_promo_service.apply_order_promotion.return_value = 150.0

        response = client.get("/promotions/order/o1/apply")

    assert response.status_code == 200
    assert response.json()["final_total"] == 150.0

def test_api_apply_nonexistent_order_promotion():
    with patch("app.api.routes.promotion_route.order_service") as mock_order_service:
        mock_order_service.get_order.return_value = None
        response = client.get("/promotions/order/o1/apply")

    assert response.status_code == 404
    assert response.json()["detail"] == "Order not found"