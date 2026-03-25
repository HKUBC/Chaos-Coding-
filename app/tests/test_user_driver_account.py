import pytest
from app.model.driver import Driver
from app.model.user_role import UserRole
from app.repositories.user_repository import UserRepository
from app.services.data_service import DataService


class FakeDataService(DataService):
    def load_data(self) -> list[dict]:
        return []


def test_driver_has_correct_fields():
    driver = Driver(driver_id="d1", name="John")
    assert driver.driver_id == "d1"
    assert driver.name == "John"
    assert driver.role == UserRole.DRIVER


def test_driver_can_be_added_to_repository():
    repo = UserRepository(FakeDataService())
    repo.add_driver(Driver(driver_id="d1", name="John"))
    assert repo.get_driver("d1") is not None


def test_all_drivers_returns_added_drivers():
    repo = UserRepository(FakeDataService())
    repo.add_driver(Driver(driver_id="d1", name="John"))
    repo.add_driver(Driver(driver_id="d2", name="Jane"))
    assert len(repo.all_drivers()) == 2


def test_duplicate_driver_raises_error():
    repo = UserRepository(FakeDataService())
    repo.add_driver(Driver(driver_id="d1", name="John"))
    with pytest.raises(ValueError):
        repo.add_driver(Driver(driver_id="d1", name="John"))
