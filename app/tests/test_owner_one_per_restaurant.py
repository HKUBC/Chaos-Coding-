import pandas as pd
from app.repositories.user_repository import UserRepository


def test_one_owner_per_restaurant():
    df = pd.DataFrame([
        {"customer_id": "c1", "restaurant_id": "10", "age": 25, "gender": "Female", "location": "City_1"},
        {"customer_id": "c2", "restaurant_id": "20", "age": 30, "gender": "Male",   "location": "City_2"},
        {"customer_id": "c3", "restaurant_id": "10", "age": 22, "gender": "Male",   "location": "City_3"},
    ])
    repo = UserRepository(df=df)
    assert len(repo.all_owners()) == 2
