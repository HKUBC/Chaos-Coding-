import pandas as pd
from app.model.customer import Customer
from app.repositories.user_repository import UserRepository


def test_customer_can_be_added():
    repo = UserRepository(df=pd.DataFrame(columns=["customer_id", "restaurant_id", "age", "gender", "location"]))
    repo.add_customer(Customer(customer_id="c1", age=25, gender="Female", location="City_1"))
    assert repo.get_customer("c1") is not None
