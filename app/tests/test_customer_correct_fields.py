import pandas as pd
from app.repositories.user_repository import UserRepository
from app.model.user_role import UserRole


def test_customer_has_correct_fields():
    df = pd.DataFrame([
        {"customer_id": "c1", "restaurant_id": "1", "age": 25, "gender": "Female", "location": "City_1"},
    ])
    repo = UserRepository(df=df)
    customer = repo.get_customer("c1")

    assert customer.customer_id == "c1"
    assert customer.age == 25
    assert customer.gender == "Female"
    assert customer.location == "City_1"
    assert customer.role == UserRole.CUSTOMER
