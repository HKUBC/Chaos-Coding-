from fastapi import FastAPI
from app.api.routes.restaurant_route import router as restaurant_router
from app.api.routes.notification_route import router as notification_router
from app.api.routes.delivery_route import router as delivery_router
from app.api.routes.driver_route import router as driver_router
from app.api.routes.auth_route import router as auth_router

from app.services.restaurant_data_loader import load_all_restaurant

app = FastAPI()

# Routers include the prefix and tags
app.include_router(restaurant_router)
app.include_router(notification_router)
app.include_router(delivery_router)
app.include_router(driver_router)
app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "Food Delivery API running"}

restaurant_data = load_all_restaurant('app/data/restaurants.csv') #loads the restaurant data from the csv file and stores it in a dictionary, where the key is the restaurant id and the value is the restaurant object