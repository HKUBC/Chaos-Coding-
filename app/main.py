from fastapi import FastAPI, APIRouter
from app.api.routes.restaurant_route import router as restaurant_router
from app.api.routes.notification_route import router as notification_router
from app.api.routes.delivery_route import router as delivery_router
from app.services.restaurant_data_loader import load_all_restaurant

app = FastAPI()

router = APIRouter() # this is the main router for the application, it will be used to include all the other routers in the application
app.include_router(restaurant_router, prefix="/restaurants", tags=["Restaurants"])
app.include_router(notification_router, prefix="/notifications", tags=["Notifications"])
app.include_router(delivery_router, prefix="/delivery", tags=["Deliveries"])

@app.get("/")
def root():
    return {"message": "Food Delivery API running"}

restaurant_data = load_all_restaurant('app/data/restaurants.csv') #loads the restaurant data from the csv file and stores it in a dictionary, where the key is the restaurant id and the value is the restaurant object