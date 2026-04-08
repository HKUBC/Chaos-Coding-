from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from app.main import app

client = TestClient(app)

def test_api_apply_valid_item_promotion():
    mock_item = MagicMock()
    mock_item.item_id = "i1"
    mock_item.price = 100.0

    mock_order = MagicMock()
    mock_order.get_item.return_value = mock_item

    with patch("app.api.routes.promotion_route.promotion_service") as mock_promo_service, \
         patch("app.api.routes.promotion_route.order_service") as mock_order_service:

        mock_order_service.get_order.return_value = mock_order
        mock_promo_service.apply_item_promotion.return_value = 80.0

        response = client.get("/promotions/item/o1/i1/apply")

    assert response.status_code == 200
    assert response.json()["final_price"] == 80.0

def test_api_apply_nonexistent_order_item_promotion():
    with patch("app.api.routes.promotion_route.promotion_service") as mock_promo_service, \
         patch("app.api.routes.promotion_route.order_service") as mock_order_service:
        mock_promo_service.item_promotions = []
        mock_order_service.get_order.return_value = None
        response = client.get("/promotions/item/o1/i1/apply")

    assert response.status_code == 404
    assert response.json()["detail"] == "Order not found"

def test_api_apply_nonexistent_item_item_promotion():
    mock_order = MagicMock()
    mock_order.get_item.return_value = None

    with patch("app.api.routes.promotion_route.promotion_service") as mock_promo_service, \
         patch("app.api.routes.promotion_route.order_service") as mock_order_service:

        mock_order_service.get_order.return_value = mock_order
        response = client.get("/promotions/item/o1/i1/apply")

    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"