from app.model.promotion import Promotion
from app.model.order import Order

class OrderPromotion(Promotion):
    def __init__(self, promo_id: str, discount_type: str, value: float, min_total = 0):
        """
        discount_types: 'percent' or 'fixed'
        value: use decimal for percent (0.2 for 20% off) or dollar amount for fixed (5 for $5 off)
        min_total: minimum that the order total must be for the promotion to apply
        """

        super().__init__(promo_id)
        self.discount_type = discount_type
        self.value = value
        self.min_total = min_total

    def is_valid(self, order: Order) -> bool:
        return order.order_total() >= self.min_total

    def apply(self, total: float) -> float:
        if total < self.min_total:
            return total

        if self.discount_type == "percent":
            return round(total * (1 - self.value), 2)       # round to 2 decimal places for currency
        
        if self.discount_type == "fixed":
            return max(0, round(total - self.value, 2))     # don't allow negative prices
        
        return total