import pytest
from unittest.mock import MagicMock
from app.model.item import Item
from app.model.order import Order
from app.model.promotion import Promotion
from app.model.item_promotion import ItemPromotion
from app.model.order_promotion import OrderPromotion
from app.services.promotion_service import PromotionService

# ----- Fixtures for examples and reusable tests -----
@pytest.fixture
def example_order():
    return Order(order_id="o1", customer_id="c1", restaurant_id="r1")

# ----- Test cases for Order class -----
def test_order_total_with_item_promotion(example_order):
    item = MagicMock(spec=Item)
    item.item_id = "i1"
    item.total_price.return_value = 10

    example_order.add_item(item)

    promo_service = PromotionService()
    promo_service.item_promotions.append(ItemPromotion("p1", "i1", 0.2))

    total = example_order.order_total(promo_service)
    assert total == 8.0

def test_order_total_with_order_promotion(example_order):
    item1 = MagicMock(spec=Item)
    item1.item_id = "i1"
    item1.total_price.return_value = 10

    item2 = MagicMock(spec=Item)
    item2.item_id = "i2"
    item2.total_price.return_value = 20

    example_order.add_item(item1)
    example_order.add_item(item2)

    promo_service = PromotionService()
    promo_service.order_promotions.append(OrderPromotion("p1", "fixed", 5, 0))

    total = example_order.order_total(promo_service)
    assert total == 25.0

def test_order_total_with_item_and_order_promotion(example_order):
    item1 = MagicMock(spec=Item)
    item1.item_id = "i1"
    item1.total_price.return_value = 10

    item2 = MagicMock(spec=Item)
    item2.item_id = "i2"
    item2.total_price.return_value = 20

    example_order.add_item(item1)
    example_order.add_item(item2)

    promo_service = PromotionService()
    promo_service.item_promotions.append(ItemPromotion("p1", "i2", 0.5))
    promo_service.order_promotions.append(OrderPromotion("p1", "percent", 0.2, 0))

    total = example_order.order_total(promo_service)
    assert total == 16.0