from app.model.driver import Driver
from app.repositories.user_repository import UserRepository
from app.services.delivery_service import DeliveryService

repo = UserRepository()
delivery_service = DeliveryService()


# The DriverService is responsible for managing the drivers and their assignments to deliveries. 
# It provides methods to create a driver, get a driver by id, get all drivers, and assign a driver to a delivery.
class DriverService:

    # Creates a new driver with the given id and name. Raises a ValueError if a driver with the same id already exists.
    def create_driver(self, driver_id: str, name: str) -> Driver:
        driver = Driver(driver_id=driver_id, name=name)
        repo.add_driver(driver)
        return driver
    
    # Retrieves a driver by their id. Returns None if the driver doesn't exist.
    def get_driver(self, driver_id: str) -> Driver | None:
        return repo.get_driver(driver_id)

    # Retrieves a list of all drivers in the system.
    def get_all_drivers(self) -> list[Driver]:
        return repo.all_drivers()
    
    # Assigns a driver to a delivery for a given order id. Raises a ValueError if the delivery or driver doesn't exist, or if the assignment is invalid.
    def assign_driver_to_delivery(self, order_id: str, driver_id: str):
        delivery = delivery_service.get_delivery(order_id)
        if delivery is None:
            raise ValueError(f"No delivery found for order {order_id}.")

        driver = self.get_driver(driver_id)
        if driver is None:
            raise ValueError(f"Driver {driver_id} not found.")

        delivery.assign_driver(driver)
        return delivery
    
