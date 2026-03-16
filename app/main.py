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

@app.get("/restaurants/{restaurant_id}/menu")
# this route method will get the menu of a restaurant by its id, it also allows for filtering the menu by food item, cuisine, order time, and price range, if the restaurant is not found or is closed then it will return a 404 error
def get_filtered_menu(
    restaurant_id: int,
    food_item: str = None,
    cuisine: str = None,
    order_time: str = None,
    min_price: float = None,
    max_price: float = None
):

    result = service.filter_items(
        restaurant_id,
        food_item,
        cuisine,
        order_time,
        min_price,
        max_price
    )

    if result is None:
        raise HTTPException(status_code=404, detail="Restaurant not found or closed")

    return result