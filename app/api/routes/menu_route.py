from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.model.item import Item
from app.services.restaurant_data_loader import load_all_restaurant

router = APIRouter(prefix="/menu", tags=["Menu"])

restaurant_data = load_all_restaurant('app/data/restaurants.csv')


class AddItemRequest(BaseModel):
    item_id: str
    name: str
    price: float
    quantity: int = 1


@router.get("/{restaurant_id}")
def get_menu(restaurant_id: int):
    restaurant = restaurant_data.get(restaurant_id)
    if restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    if restaurant.menu is None:
        raise HTTPException(status_code=404, detail="Menu not found")
    return {"restaurant_id": restaurant_id, "items": [repr(i) for i in restaurant.menu.get_all_items()]}


@router.post("/{restaurant_id}/items")
def add_item(restaurant_id: int, request: AddItemRequest):
    restaurant = restaurant_data.get(restaurant_id)
    if restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    if restaurant.menu is None:
        raise HTTPException(status_code=404, detail="Menu not found")
    try:
        item = Item(
            item_id=request.item_id,
            name=request.name,
            price=request.price,
            quantity=request.quantity
        )
        restaurant.menu.add_item(item)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"message": f"Item '{request.name}' added to menu"}


@router.delete("/{restaurant_id}/items/{item_id}")
def remove_item(restaurant_id: int, item_id: str):
    restaurant = restaurant_data.get(restaurant_id)
    if restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    if restaurant.menu is None:
        raise HTTPException(status_code=404, detail="Menu not found")
    item = restaurant.menu.get_item_by_id(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    restaurant.menu.items.remove(item)
    return {"message": f"Item {item_id} removed from menu"}
