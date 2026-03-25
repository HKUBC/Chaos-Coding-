import pandas as pd
from app.model.restaurant_owner import RestaurantOwner
from app.repositories.user_repository import UserRepository


def test_owner_can_be_added():
    repo = UserRepository(df=pd.DataFrame(columns=["customer_id", "restaurant_id", "age", "gender", "location"]))
    repo.add_owner(RestaurantOwner(owner_id="owner_1", restaurant_id="1"))
    assert repo.get_owner_by_restaurant("1") is not None
