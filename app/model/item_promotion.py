from app.model.promotion import Promotion
from app.model.item import Item

class ItemPromotion(Promotion):
    def __init__(self, promo_id: str, item_id: str, discount: float):
        super().__init__(promo_id)
        self.item_id = item_id
        self.discount = discount

    def apply(self, total: float) -> float:
        return round(total * (1 - self.discount), 2)