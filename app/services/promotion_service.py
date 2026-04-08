from app.model.promotion import Promotion
from app.model.order_promotion import OrderPromotion
from app.model.item_promotion import ItemPromotion
from app.model.item import Item
from app.model.order import Order

class PromotionService:
    def __init__(self):
        self.item_promotions:  list[ItemPromotion]  = []  # item_id gives all promotions for that item
        self.order_promotions: list[OrderPromotion] = []  # order_id gives all promotions for that order

    # ITEM PROMOTIONS
    def get_item_promotions(self, item_id: str) -> list[ItemPromotion]:
        return [promo for promo in self.item_promotions
                if promo.item_id == item_id]
    
    def apply_item_promotion(self, item: Item) -> float:
        price = item.total_price()
        promos = self.get_item_promotions(item.item_id)

        for promo in promos:
            price = promo.apply(price)
        
        return price    # no promotion, return original price
    
    # ORDER PROMOTIONS
    def apply_order_promotion(self, order: Order, total: float) -> float:
        for promo in self.order_promotions:
            if promo.is_valid(order):
                total = promo.apply(total)
        return total