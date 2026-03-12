from fastapi import APIRouter, HTTPException
from app.services.restaurant_service import RestaurantService

router = APIRouter(prefix="/restaurants")

service = RestaurantService()