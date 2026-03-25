import pandas as pd
from app.repositories.user_repository import UserRepository
from app.model.user_role import UserRole


def test_owner_has_correct_fields():
    df = pd.DataFrame([
        {"customer_id": "c1", "restaurant_id": "10", "age": 25, "gender": "Female", "location": "City_1"},
    ])
    repo = UserRepository(df=df)
    owner = repo.get_owner_by_restaurant("10")

    assert owner.restaurant_id == "10"
    assert owner.owner_id == "owner_10"
    assert owner.role == UserRole.RESTAURANT_OWNER
