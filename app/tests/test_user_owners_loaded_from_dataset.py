from app.repositories.user_repository import UserRepository
from app.services.data_service import DataService
from app.model.user_role import UserRole


class FakeDataService(DataService):
    def load_data(self) -> list[dict]:
        return [
            {"customer_id": "c1", "restaurant_id": "10", "age": "25", "gender": "Female", "location": "City_1"},
            {"customer_id": "c2", "restaurant_id": "20", "age": "30", "gender": "Male",   "location": "City_2"},
            {"customer_id": "c3", "restaurant_id": "10", "age": "22", "gender": "Male",   "location": "City_3"},  # same restaurant
        ]


def test_one_owner_per_restaurant():
    repo = UserRepository(FakeDataService())

    # restaurants 10 and 20 — should be exactly 2 owners
    assert len(repo.all_owners()) == 2


def test_owner_has_correct_fields():
    repo = UserRepository(FakeDataService())
    owner = repo.get_owner_by_restaurant("10")

    assert owner.restaurant_id == "10"
    assert owner.owner_id == "owner_10"
    assert owner.role == UserRole.RESTAURANT_OWNER
