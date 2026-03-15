from fastapi import FastAPI
from app.routes.restaurant import router as restaurant_router

app = FastAPI()

app.include_router(restaurant_router)

@app.get("/")
def root():
    return {"message": "Food Delivery API running"}