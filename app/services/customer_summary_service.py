from app.model.order import Order
from app.model.order_summary import OrderSummary
from app.services.order_service import OrderService

class CustomerSummaryService:
    """
    Manages the summary of an order which include pricing, promotions, taxes, and fees
    """

    # Returns the summary of an order
    def get_sorted_summary(self, customer_id: str) -> list[OrderSummary]:
        orders = OrderService().get_orders_by_customer(customer_id) or []
        orders_with_date = [o for o in orders if o.order_date is not None]
        sorted_orders = sorted(orders_with_date, key = lambda o: o.order_date, reverse = True)

        return [OrderSummary(order) for order in sorted_orders]