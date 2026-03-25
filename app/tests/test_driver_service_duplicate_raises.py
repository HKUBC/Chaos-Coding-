import pytest
from app.services.driver_service import DriverService

def test_driver_service_duplicate_raises():
    service = DriverService()
    service.create_driver("d_test4", "Bob")
    with pytest.raises(ValueError):
        service.create_driver("d_test4", "Bob")