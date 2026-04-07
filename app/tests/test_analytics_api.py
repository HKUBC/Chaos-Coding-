import pandas as pd
import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app

client = TestClient(app)

SAMPLE_DATA = {
    "order_id":      ["o1", "o2", "o3"],
    "restaurant_id": [16,   16,   16],
    "food_item":     ["Pasta", "Pasta", "Burger"],
    "order_value":   [10.00, 20.00, 30.00],
}

# helper to patch the service in route tests, so we never read the real CSV

def _mock_service(df=None, session_orders=None):
    """Patch AnalyticsService so tests never read the real CSV."""
    from app.services.analytics_service import AnalyticsService
    return AnalyticsService(
        df=df if df is not None else pd.DataFrame(SAMPLE_DATA),
        session_orders=session_orders or {},
    )

# valid restaurant

def test_dashboard_returns_200_for_valid_restaurant():
    with patch("app.api.routes.analytics_route.analytics_service", _mock_service()):
        response = client.get("/analytics/16/dashboard")
    assert response.status_code == 200


def test_dashboard_response_has_all_required_fields():
    with patch("app.api.routes.analytics_route.analytics_service", _mock_service()):
        data = client.get("/analytics/16/dashboard").json()
    expected_keys = {
        "restaurant_id",
        "total_revenue",
        "most_popular_dish",
        "total_orders",
        "active_orders",
        "average_order_value",
    }
    assert expected_keys.issubset(data.keys())


def test_dashboard_restaurant_id_matches_request():
    with patch("app.api.routes.analytics_route.analytics_service", _mock_service()):
        data = client.get("/analytics/16/dashboard").json()
    assert data["restaurant_id"] == "16"


def test_dashboard_total_revenue_is_correct():
    with patch("app.api.routes.analytics_route.analytics_service", _mock_service()):
        data = client.get("/analytics/16/dashboard").json()
    assert data["total_revenue"] == 60.00


def test_dashboard_most_popular_dish_is_correct():
    with patch("app.api.routes.analytics_route.analytics_service", _mock_service()):
        data = client.get("/analytics/16/dashboard").json()
    assert data["most_popular_dish"] == "Pasta"


def test_dashboard_total_orders_is_correct():
    with patch("app.api.routes.analytics_route.analytics_service", _mock_service()):
        data = client.get("/analytics/16/dashboard").json()
    assert data["total_orders"] == 3


def test_dashboard_average_order_value_is_correct():
    with patch("app.api.routes.analytics_route.analytics_service", _mock_service()):
        data = client.get("/analytics/16/dashboard").json()
    assert data["average_order_value"] == 20.00


def test_dashboard_active_orders_is_zero_with_no_session():
    with patch("app.api.routes.analytics_route.analytics_service", _mock_service()):
        data = client.get("/analytics/16/dashboard").json()
    assert data["active_orders"] == 0

#unknown restaurant

def test_dashboard_returns_404_for_unknown_restaurant():
    with patch("app.api.routes.analytics_route.analytics_service", _mock_service()):
        response = client.get("/analytics/9999/dashboard")
    assert response.status_code == 404


def test_dashboard_404_detail_mentions_not_found():
    with patch("app.api.routes.analytics_route.analytics_service", _mock_service()):
        data = client.get("/analytics/9999/dashboard").json()
    assert "not found" in data["detail"].lower()
