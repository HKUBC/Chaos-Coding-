import pytest
import pandas as pd
from app.model.driver import Driver
from app.repositories.user_repository import UserRepository


def test_duplicate_driver_raises_error():
    repo = UserRepository(df=pd.DataFrame(columns=["customer_id", "restaurant_id", "age", "gender", "location"]))
    repo.add_driver(Driver(driver_id="d1", name="John"))
    with pytest.raises(ValueError):
        repo.add_driver(Driver(driver_id="d1", name="John"))
