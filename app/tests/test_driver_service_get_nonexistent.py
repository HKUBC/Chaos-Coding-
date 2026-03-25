from app.services.driver_service import DriverService

def test_driver_service_get_nonexistent():
    service = DriverService()
    driver = service.get_driver("nonexistent_999")
    assert driver is None