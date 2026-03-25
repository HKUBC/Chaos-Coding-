import pytest
import pandas as pd
from app.model.restaurant_owner import RestaurantOwner
from app.repositories.user_repository import UserRepository


def test_duplicate_owner_raises_error():
    repo = UserRepository(df=pd.DataFrame(columns=["customer_id", "restaurant_id", "age", "gender", "location"]))
    repo.add_owner(RestaurantOwner(owner_id="owner_1", restaurant_id="1"))
    with pytest.raises(ValueError):
        repo.add_owner(RestaurantOwner(owner_id="owner_1", restaurant_id="1"))
