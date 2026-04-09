from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from pydantic import BaseModel
from app.services.restaurant_service import RestaurantService
from app.repositories.restaurant_repository import RestaurantRepository

router = APIRouter(prefix="/restaurants", tags=["Restaurants"])
service = RestaurantService()

@router.get("/all_restaurants")
# this route method will get all the restaurants in the system, if there are no restaurants then it will return an empty list
async def get_all_restaurants():

        restaurants = service.get_all_restaurants()

        return restaurants

@router.get("/favorites")
def get_favorites():

    return service.get_favorites()

@router.post("/{restaurant_id}/favorite")
# this route method will add a restaurant to the user's favorites, it checks if the restaurant exists and is open before adding
# it to the favorites, if the restaurant is not found then it will return a 404 error
def favorite_restaurant(restaurant_id: int):

    result = service.favorite_restaurant(restaurant_id)

    if not result:
        raise HTTPException(status_code=404, detail="Restaurant not found")

    return {"message": "Restaurant added to favorites"}

@router.delete("/{restaurant_id}/favorite")
# this route method will remove a restaurant from the user's favorites, it checks if the restaurant exists and is open before removing
def unfavorite_restaurant(restaurant_id: int):

    result = service.unfavorite_restaurant(restaurant_id)

    if not result:
        raise HTTPException(status_code=404, detail="Favorite not found")

    return {"message": "Restaurant removed from favorites"}

@router.get("/{restaurant_id}")
# this route method will get a single restaurant by its id, if the restaurant is not found then it will return a 404 error
async def get_restaurant(restaurant_id: int):

        restaurant = service.get_restaurant(restaurant_id)

        if restaurant is None:
            raise HTTPException(status_code=404, detail="Restaurant not found")

        return restaurant

@router.get("/{restaurant_id}/items/filter")
async def filter_menu_items(
    restaurant_id: int,
    food_item: Optional[str] = Query(None),
    cuisine: Optional[str] = Query(None),
    min_price: Optional[float] = Query(None),
    max_price: Optional[float] = Query(None),
):
    result = service.filter_items(restaurant_id, food_item, cuisine, None, min_price, max_price)

    if result is None:
        raise HTTPException(status_code=404, detail="Restaurant not found or not open")

    return result

class ToggleItemRequest(BaseModel):
    food_item: str

@router.post("/{restaurant_id}/items/toggle")
async def toggle_item_availability(restaurant_id: int, request: ToggleItemRequest):
    if not service.get_restaurant(restaurant_id) and not service.filter_items(restaurant_id):
        raise HTTPException(status_code=404, detail="Restaurant not found")
    is_available = service.toggle_item_availability(restaurant_id, request.food_item)
    return {"food_item": request.food_item, "available": is_available}

@router.get("/{restaurant_id}/items/unavailable")
async def get_unavailable_items(restaurant_id: int):
    return service.get_unavailable_items(restaurant_id)

# this route method is to get the profile of a restaurant with its menu
@router.get("/{restaurant_id}/profile")
async def get_restaurant_profile(restaurant_id: int, cuisine: str | None = None):

     restaurant = service.get_restaurant(restaurant_id)
     if not restaurant:
         raise HTTPException(status_code=404, detail="Restaurant not available")

     menu = service.get_menu(restaurant_id)
     if not menu:
         raise HTTPException(status_code=404, detail="Menu not available")
     return {
        "restaurant": restaurant,
        "menu": menu
    }
