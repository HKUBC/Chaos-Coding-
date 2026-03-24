from fastapi import APIRouter, HTTPException
from app.services.restaurant_service import RestaurantService
from app.repositories.restaurant_repository import RestaurantRepository


router = APIRouter(prefix="/restaurants")
service = RestaurantService()

@router.get("/{restaurant_id}")
# this route method will get a single restaurant by its id, if the restaurant is not found then it will return a 404 error
async def get_restaurant(restaurant_id: int):

        restaurant = service.get_restaurant(restaurant_id)

        if restaurant is None:
            raise HTTPException(status_code=404, detail="Restaurant not found")

        return restaurant

@router.get("/all_restaurants")
# this route method will get all the restaurants in the system, if there are no restaurants then it will return an empty list
async def get_all_restaurants():

        restaurants = service.get_all_restaurants()

        return restaurants

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

@router.get("/favorites") 
# this route method will get the user's favorite restaurants, it returns a list of restaurant ids that are in the user's favorites

def get_favorites():

    return service.get_favorites()


# this route method is to get the profile of a restaurant with its menu
@router.get("/{restaurant_id}/profile")
async def get_restaurant_profile(restaurant_id: int, cuisine: str = None):
     
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
