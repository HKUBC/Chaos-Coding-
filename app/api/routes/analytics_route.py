from fastapi import APIRouter, HTTPException
from app.model.analytics import AnalyticsDashboard
from app.services.analytics_service import AnalyticsService
from app.repositories.order_repository import OrderRepository

router = APIRouter(prefix="/analytics", tags=["Analytics"])

_order_repo = OrderRepository()
analytics_service = AnalyticsService(session_orders=_order_repo._session_orders)


@router.get("/{restaurant_id}/dashboard", response_model=AnalyticsDashboard)
def get_dashboard(restaurant_id: str):
    try:
        return analytics_service.get_dashboard(restaurant_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
