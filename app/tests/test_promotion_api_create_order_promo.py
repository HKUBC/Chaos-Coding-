from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app

client = TestClient(app)

def test_api_create_valid_item_promotion():
    with patch("app.api.routes.promotion_route.promotion_service") as mock_promo_service:
        mock_promo_service.create_order_promotion.return_value = True
        response = client.post("/promotions/order/p1/percent/0.2/100")

    assert response.status_code == 200
    assert response.json()["message"] == "Order promotion p1 created successfully"

def test_api_create_invalid_promo_type():
    with patch("app.api.routes.promotion_route.promotion_service") as mock_promo_service:
        mock_promo_service.create_order_promotion.return_value = False
        response = client.post("/promotions/order/p1/free/1/100")

    assert response.status_code == 400
    assert response.json()["detail"] == "Promotion type must be 'percent' or 'fixed'"