from app.model.driver import Driver
from app.model.user_role import UserRole


def test_driver_has_correct_fields():
    driver = Driver(driver_id="d1", name="John")
    assert driver.driver_id == "d1"
    assert driver.name == "John"
    assert driver.role == UserRole.DRIVER
