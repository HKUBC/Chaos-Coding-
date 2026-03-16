from fastapi import FastAPI, APIRouter
from app.api.routes.restaurant_route import router as restaurant_router
#from app.services.restaurant_data_loader import load_restaurant

app = FastAPI()

router = APIRouter() # this is the main router for the application, it will be used to include all the other routers in the application
router.include_router(restaurant_router) # this will include the restaurant router in the main router, so that all the routes defined in the restaurant router will be available in the main router
app.include_router(restaurant_router)


@app.get("/")
def root():
    return {"message": "Food Delivery API running"}

#restaurant = load_restaurant('app/data/food_delivery.csv') #loads the restaurant data from the csv file and stores it in a dictionary, where the key is the restaurant id and the value is the restaurant object

