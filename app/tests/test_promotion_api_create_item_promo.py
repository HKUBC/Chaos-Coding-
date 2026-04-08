from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from app.main import app

client = TestClient(app)

def test_api_create_valid_item_promotion():
    with patch("app.api.routes.promotion_route.promotion_service") as mock_promo_service:
        mock_promo_service.create_item_promotion.return_value = True
        response = client.post("/promotions/item/p1/i1/0.2")

    assert response.status_code == 200
    assert response.json()["message"] == "Item promotion p1 created successfully"