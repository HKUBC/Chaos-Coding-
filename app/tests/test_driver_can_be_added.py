import pandas as pd
from app.model.driver import Driver
from app.repositories.user_repository import UserRepository


def test_driver_can_be_added_to_repository():
    repo = UserRepository(df=pd.DataFrame(columns=["customer_id", "restaurant_id", "age", "gender", "location"]))
    repo.add_driver(Driver(driver_id="d1", name="John"))
    assert repo.get_driver("d1") is not None
