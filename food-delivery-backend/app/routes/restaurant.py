from fastapi import APIRouter, HTTPException
from app.services.restaurant_service import RestaurantService

router = APIRouter(prefix="/restaurants")

service = RestaurantService()

@router.get("/{restaurant_id}")
def get_restaurant(restaurant_id: int):

    restaurant = service.get_restaurant(restaurant_id)

    if restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")

    return restaurant