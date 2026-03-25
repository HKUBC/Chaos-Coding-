import pandas as pd
from app.repositories.user_repository import UserRepository


def test_customers_loaded_from_dataset():
    df = pd.DataFrame([
        {"customer_id": "c1", "restaurant_id": "1", "age": 25, "gender": "Female", "location": "City_1"},
        {"customer_id": "c2", "restaurant_id": "2", "age": 30, "gender": "Male",   "location": "City_2"},
        {"customer_id": "c1", "restaurant_id": "1", "age": 25, "gender": "Female", "location": "City_1"},
    ])
    repo = UserRepository(df=df)
    assert len(repo.all_customers()) == 2
