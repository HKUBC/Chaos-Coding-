from app.repositories.user_repository import UserRepository
from app.services.data_service import DataService
from app.model.user_role import UserRole


class FakeDataService(DataService):
    def load_data(self) -> list[dict]:
        return [
            {"customer_id": "c1", "restaurant_id": "1", "age": "25", "gender": "Female", "location": "City_1"},
            {"customer_id": "c2", "restaurant_id": "2", "age": "30", "gender": "Male",   "location": "City_2"},
            {"customer_id": "c1", "restaurant_id": "1", "age": "25", "gender": "Female", "location": "City_1"},  # duplicate
        ]


def test_customers_loaded_from_dataset():
    repo = UserRepository(FakeDataService())

    # c1 appears twice but should only be stored once
    assert len(repo.all_customers()) == 2


def test_customer_has_correct_fields():
    repo = UserRepository(FakeDataService())
    customer = repo.get_customer("c1")

    assert customer.customer_id == "c1"
    assert customer.age == 25
    assert customer.gender == "Female"
    assert customer.location == "City_1"
    assert customer.role == UserRole.CUSTOMER
