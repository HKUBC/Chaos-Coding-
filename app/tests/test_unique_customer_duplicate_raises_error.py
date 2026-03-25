import pytest
import pandas as pd
from app.model.customer import Customer
from app.repositories.user_repository import UserRepository


def test_duplicate_customer_raises_error():
    repo = UserRepository(df=pd.DataFrame(columns=["customer_id", "restaurant_id", "age", "gender", "location"]))
    repo.add_customer(Customer(customer_id="c1", age=25, gender="Female", location="City_1"))
    with pytest.raises(ValueError):
        repo.add_customer(Customer(customer_id="c1", age=30, gender="Male", location="City_2"))
