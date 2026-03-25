from app.services.driver_service import DriverService

def test_driver_service_get_driver():
    service = DriverService()
    service.create_driver("d_test2", "Jane")
    driver = service.get_driver("d_test2")
    assert driver is not None
    assert driver.name == "Jane"