import pytest
from app.services.order_service import OrderService

def test_reorder_nonexistent_order_raises():
    service = OrderService()
    with pytest.raises(ValueError):
        service.reorder("cust_1", "nonexistent", "o2")