from fastapi import APIRouter, HTTPException
from app.services.restaurant_service import RestaurantService
from app.repositories.restaurant_repository import RestaurantRepository
service = RestaurantService()


router = APIRouter(prefix="/restaurants")
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

def favorite_restaurant(restaurant_id: int):

    return {"success": service.favorite_restaurant(restaurant_id)}



@router.delete("/{restaurant_id}/favorite")

def remove_favorite(restaurant_id: int):

    return {"success": service.unfavorite_restaurant(restaurant_id)}


@router.get("/{restaurant_id}")
# this route method will get a single restaurant by its id, if the restaurant is not found then it will return a 404 error
async def get_restaurant(restaurant_id: int):

        restaurant = service.get_restaurant(restaurant_id)

        if restaurant is None:
            raise HTTPException(status_code=404, detail="Restaurant not found")

        return restaurant

