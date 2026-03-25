import pytest
from unittest.mock import MagicMock, patch
from datetime import datetime, timedelta

from app.model.item import Item
from app.model.order import Order
from app.model.order_summary import OrderSummary
from app.services.customer_summary_service import CustomerSummaryService

# ----- Fixtures for example orders and service -----
@pytest.fixture
def order1():
    order = Order("o1", "c1", "r1")
    order.items.append(MagicMock(spec=Item, total_price=MagicMock(return_value=10.0), item_id="i1"))
    order.order_date = datetime.now() - timedelta(days=2)
    return order

@pytest.fixture
def order2():
    order = Order("o2", "c1", "r2")
    order.items.append(MagicMock(spec=Item, total_price=MagicMock(return_value=30.0), item_id="i2"))
    order.order_date = datetime.now() - timedelta(days=1)
    return order

@pytest.fixture
def order3():
    order = Order("o3", "c1", "r3")
    order.items.append(MagicMock(spec=Item, total_price=MagicMock(return_value=8.0), item_id="i3"))
    order.order_date = datetime.now()
    return order

# ----- Test cases for CustomerSummary Class -----
def test_get_sorted_summary_with_valid_customer_id(order1, order2, order3):
    service = CustomerSummaryService()

    with patch("app.services.customer_summary_service.OrderService") as MockOrderService:
        mock_service_instance = MockOrderService.return_value
        mock_service_instance.get_orders_by_customer.return_value = [order1, order2, order3]

        summaries = service.get_sorted_summary("c1")

    assert len(summaries) == 3

    # Checking in order of latest date
    assert summaries[0].order_id == "o3"
    assert summaries[1].order_id == "o2"
    assert summaries[2].order_id == "o1"