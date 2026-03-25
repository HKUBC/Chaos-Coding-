from app.services.driver_service import DriverService

def test_driver_service_create_driver():
    service = DriverService()
    driver = service.create_driver("d_test1", "John")
    assert driver.driver_id == "d_test1"
    assert driver.name == "John"