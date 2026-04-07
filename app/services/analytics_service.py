import os
import pandas as pd
from app.model.analytics import AnalyticsDashboard
from app.model.order_status import OrderStatus


ACTIVE_STATUSES = {OrderStatus.PENDING, OrderStatus.PREPARING, OrderStatus.DELIVERING}


class AnalyticsService:

    def __init__(self, df: pd.DataFrame | None = None, session_orders: dict | None = None):
        if df is not None:
            self._df = df
        else:
            current_dir = os.path.dirname(__file__)
            data_path = os.path.join(current_dir, "..", "data", "food_delivery.csv")
            self._df = pd.read_csv(data_path)

        # session_orders is injected so the service can count live in-memory orders.
        # In production this is the OrderRepository._session_orders dict.
        self._session_orders: dict = session_orders if session_orders is not None else {}

    def get_dashboard(self, restaurant_id: str) -> AnalyticsDashboard:
        restaurant_df = self._df[self._df["restaurant_id"].astype(str) == str(restaurant_id)]

        if restaurant_df.empty:
            raise ValueError(f"Restaurant '{restaurant_id}' not found.")

        total_revenue = round(float(restaurant_df["order_value"].sum()), 2)
        most_popular_dish = restaurant_df["food_item"].value_counts().idxmax()
        total_orders = int(restaurant_df["order_id"].nunique())
        average_order_value = round(float(restaurant_df["order_value"].mean()), 2)
        active_orders = self._count_active_orders(restaurant_id)

        return AnalyticsDashboard(
            restaurant_id=str(restaurant_id),
            total_revenue=total_revenue,
            most_popular_dish=most_popular_dish,
            total_orders=total_orders,
            active_orders=active_orders,
            average_order_value=average_order_value,
        )

    def _count_active_orders(self, restaurant_id: str) -> int:
        count = 0
        for orders in self._session_orders.values():
            for order in orders:
                if (
                    str(order.restaurant_id) == str(restaurant_id)
                    and order.status in ACTIVE_STATUSES
                ):
                    count += 1
        return count
