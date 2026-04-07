import pandas as pd
import pytest
from app.services.analytics_service import AnalyticsService
from app.model.analytics import AnalyticsDashboard
from app.model.order import Order
from app.model.item import Item
from app.model.order_status import OrderStatus


#created fake date for the test
SAMPLE_DATA = {
    "order_id":      ["o1", "o2", "o3", "o4", "o5"],
    "restaurant_id": [16,   16,   16,   99,   99],
    "food_item":     ["Pasta", "Pasta", "Burger", "Pizza", "Pizza"],
    "order_value":   [10.00, 20.00, 30.00, 15.00, 25.00],
}


@pytest.fixture
def sample_df():
    return pd.DataFrame(SAMPLE_DATA)


@pytest.fixture
def service(sample_df):
    return AnalyticsService(df=sample_df, session_orders={})


#dashboard

def test_get_dashboard_returns_analytics_dashboard(service):
    result = service.get_dashboard("16")
    assert isinstance(result, AnalyticsDashboard)

#total revencue
def test_total_revenue_sums_order_values(service):
    result = service.get_dashboard("16")
    # o1 + o2 + o3 = 10 + 20 + 30 = 60.00
    assert result.total_revenue == 60.00


#popular dish   

def test_most_popular_dish_returns_most_frequent_item(service):
    result = service.get_dashboard("16")
    # Pasta appears twice, Burger once → Pasta wins
    assert result.most_popular_dish == "Pasta"


#total orders
def test_total_orders_counts_unique_order_ids(service):
    result = service.get_dashboard("16")
    assert result.total_orders == 3  # o1, o2, o3


#average order value
def test_average_order_value_is_mean_of_order_values(service):
    result = service.get_dashboard("16")
    # (10 + 20 + 30) / 3 = 20.00
    assert result.average_order_value == 20.00


#active orders

def _make_order(order_id, customer_id, restaurant_id, status):
    order = Order(order_id=order_id, customer_id=customer_id, restaurant_id=restaurant_id)
    order.status = status
    return order


def test_active_orders_counts_pending_preparing_delivering(sample_df):
    session = {
        "c1": [
            _make_order("o10", "c1", "16", OrderStatus.PENDING),
            _make_order("o11", "c1", "16", OrderStatus.PREPARING),
            _make_order("o12", "c1", "16", OrderStatus.DELIVERING),
        ]
    }
    svc = AnalyticsService(df=sample_df, session_orders=session)
    result = svc.get_dashboard("16")
    assert result.active_orders == 3


def test_active_orders_excludes_delivered_and_cancelled(sample_df):
    session = {
        "c1": [
            _make_order("o10", "c1", "16", OrderStatus.DELIVERED),
            _make_order("o11", "c1", "16", OrderStatus.CANCELLED),
            _make_order("o12", "c1", "16", OrderStatus.CREATING),
        ]
    }
    svc = AnalyticsService(df=sample_df, session_orders=session)
    result = svc.get_dashboard("16")
    assert result.active_orders == 0


def test_active_orders_only_counts_matching_restaurant(sample_df):
    session = {
        "c1": [
            _make_order("o10", "c1", "16", OrderStatus.PENDING),
            _make_order("o11", "c1", "99", OrderStatus.PENDING),  # different restaurant
        ]
    }
    svc = AnalyticsService(df=sample_df, session_orders=session)
    result = svc.get_dashboard("16")
    assert result.active_orders == 1


def test_active_orders_zero_when_no_session_orders(service):
    result = service.get_dashboard("16")
    assert result.active_orders == 0


#unknown restaurant
def test_unknown_restaurant_raises_value_error(service):
    with pytest.raises(ValueError, match="not found"):
        service.get_dashboard("999")


#restaurant_id type mismatch between CSV and route

def test_restaurant_id_string_matches_int_in_csv(sample_df):
    # CSV has integer restaurant_ids; route passes them as strings
    svc = AnalyticsService(df=sample_df, session_orders={})
    result = svc.get_dashboard("99")
    assert result.total_revenue == 40.00   # 15 + 25
