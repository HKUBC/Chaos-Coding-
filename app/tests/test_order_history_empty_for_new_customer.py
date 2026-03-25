from app.services.order_service import OrderService

def test_order_history_empty_for_new_customer():
    service = OrderService()
    assert service.get_order_history("cust_99") == []