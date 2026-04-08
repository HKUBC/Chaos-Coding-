from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.api.routes.notification_route import router as notification_router
from app.api.routes.restaurant_route import router as restaurant_router
from app.api.routes.analytics_route import router as analytics_router
from app.api.routes.promotion_route import router as promotion_router
from app.api.routes.delivery_route import router as delivery_router
from app.api.routes.driver_route import router as driver_router
from app.api.routes.order_route import router as order_router
from app.api.routes.auth_route import router as auth_router
from app.api.routes.menu_route import router as menu_router

from app.services.restaurant_data_loader import load_all_restaurant

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

# Routers include the prefix and tags
app.include_router(notification_router)
app.include_router(restaurant_router)
app.include_router(analytics_router)
app.include_router(promotion_router)
app.include_router(delivery_router)
app.include_router(driver_router)
app.include_router(order_router)
app.include_router(auth_router)
app.include_router(menu_router)

@app.get("/")
def root():
    return FileResponse("frontend/index.html")

restaurant_data = load_all_restaurant('app/data/restaurants.csv') #loads the restaurant data from the csv file and stores it in a dictionary, where the key is the restaurant id and the value is the restaurant object