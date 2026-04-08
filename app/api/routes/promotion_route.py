from fastapi import APIRouter, HTTPException
from app.model.item_promotion import ItemPromotion
from app.model.order_promotion import OrderPromotion
from app.services.order_service import OrderService
from app.services.promotion_service import PromotionService

router = APIRouter(prefix="/promotions", tags=["Promotions"])
order_service = OrderService()
promotion_service = PromotionService()

# ITEM PROMOTION ROUTES
@router.post("/item/{promo_id}/{item_id}/{discount}")
def create_item_promotion(promo_id: str, item_id: str, discount: float):
    promo = ItemPromotion(
        promo_id=promo_id,
        item_id=item_id,
        discount=discount
    )
    promotion_service.item_promotions.append(promo)
    return {"message": f"Item promotion {promo.promo_id} created successfully"}

@router.delete("/item/{promo_id}")
def delete_item_promotion(promo_id: str):
    before = len(promotion_service.item_promotions)

    promotion_service.item_promotions = [p for p in promotion_service.item_promotions
                                        if p.promo_id != promo_id]
    
    after = len(promotion_service.item_promotions)

    if before == after:
        raise HTTPException(status_code = 404, detail = "Item promotion wasn't found")
    return {"message": f"Item promotion {promo_id} deleted successfully"}

# ORDER PROMOTION ROUTES
@router.post("/order/{promo_id}/{promo_type}/{value}/{min_total}")
def create_order_promotion(promo_id: str, promo_type: str, value: float, min_total: float = 0):
    if promo_type not in ["percent", "fixed"]:
        raise HTTPException(status_code = 400, detail = "Promotion type must be 'percent' or 'fixed'")
    
    promo = OrderPromotion(
        promo_id=promo_id,
        promo_type=promo_type,
        value=value,
        min_total=min_total
    )
    promotion_service.order_promotions.appeend(promo)
    return {"message": f"Order promotion {promo.promo_id} created successfully"}

@router.delete("/order/{promo_id}")
def delete_order_promotion(promo_id: str):
    before = len(promotion_service.order_promotions)

    promotion_service.order_promotions = [p for p in promotion_service.order_promotions
                                        if p.promo_id != promo_id]
    
    after = len(promotion_service.order_promotions)

    if before == after:
        raise HTTPException(status_code = 404, detail = "Order promotion wasn't found")
    return {"message": f"Order promotion {promo_id} deleted successfully"}

# APPLY PROMOTION ROUTES
@router.get("/item/{order_id}/{item_id}/apply")
def apply_item_promotion(order_id: str,item_id: str):
    order = order_service.get_order(order_id)
    if not order:
        raise HTTPException(status_code = 404, detail = "Order not found")

    item = order.get_item(item_id)
    if not item:
        raise HTTPException(status_code = 404, detail = "Item not found")
    
    og_price = item.total_price()
    final_price = promotion_service.apply_item_promotion(item)
    return {
        "item_id": item_id,
        "original_price": og_price,
        "final_price": final_price
    }

@router.get("/order/{order_id}/apply")
def apply_order_promotion(order_id: str):
    order = order_service.get_order(order_id)

    if not order:
        raise HTTPException(status_code = 404, detail = "Order not found")
    
    og_total = order.order_total()
    final_total = promotion_service.apply_order_promotion(order, og_total)
    return {
        "order_id": order_id,
        "original_total": og_total,
        "final_total": final_total
    }