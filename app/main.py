from fastapi import FastAPI
from app.services.restaurant_data_loader import load_restaurant



restaurant = load_restaurant('app/data/restaurants.csv') #loads the restaurant data from the csv file and stores it in a dictionary, where the key is the restaurant id and the value is the restaurant object

app = FastAPI()

@app.get("/")
def read_root():
    return {"PAGE": "Home"}


