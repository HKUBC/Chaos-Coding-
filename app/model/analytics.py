from pydantic import BaseModel


class AnalyticsDashboard(BaseModel):
    restaurant_id: str
    total_revenue: float
    most_popular_dish: str
    total_orders: int
    active_orders: int
    average_order_value: float
