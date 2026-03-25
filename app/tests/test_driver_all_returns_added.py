import pandas as pd
from app.model.driver import Driver
from app.repositories.user_repository import UserRepository


def test_all_drivers_returns_added_drivers():
    repo = UserRepository(df=pd.DataFrame(columns=["customer_id", "restaurant_id", "age", "gender", "location"]))
    repo.add_driver(Driver(driver_id="d1", name="John"))
    repo.add_driver(Driver(driver_id="d2", name="Jane"))
    assert len(repo.all_drivers()) == 2
