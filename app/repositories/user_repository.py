from app.model.customer import Customer
from app.model.restaurant_owner import RestaurantOwner
from app.model.driver import Driver
from app.services.data_service import DataService

# This repository manages all user-related data, including customers, restaurant owners, and drivers.

class UserRepository:
    def __init__(self, data_service: DataService):
        self._customers: dict[str, Customer] = {}
        self._owners: dict[str, RestaurantOwner] = {}
        self._drivers: dict[str, Driver] = {}
        self._load(data_service.load_data())

    def _load(self, rows: list[dict]):
        seen_restaurants: set[str] = set()

        for row in rows:
            # create customer if not seen before
            customer_id = row["customer_id"]
            if customer_id not in self._customers:
                self._customers[customer_id] = Customer(
                    customer_id=customer_id,
                    age=int(row["age"]),
                    gender=row["gender"],
                    location=row["location"],
                )

            # create one restaurant owner per unique restaurant
            restaurant_id = row["restaurant_id"]
            if restaurant_id not in seen_restaurants:
                seen_restaurants.add(restaurant_id)
                owner_id = f"owner_{restaurant_id}"
                self._owners[owner_id] = RestaurantOwner(
                    owner_id=owner_id,
                    restaurant_id=restaurant_id,
                )

    def get_customer(self, customer_id: str) -> Customer | None:
        return self._customers.get(customer_id)

    def get_owner_by_restaurant(self, restaurant_id: str) -> RestaurantOwner | None:
        owner_id = f"owner_{restaurant_id}"
        return self._owners.get(owner_id)

    def all_customers(self) -> list[Customer]:
        return list(self._customers.values())

    def all_owners(self) -> list[RestaurantOwner]:
        return list(self._owners.values())

    def add_driver(self, driver: Driver):
        if driver.driver_id in self._drivers:
            raise ValueError(f"Driver {driver.driver_id} already exists.")
        self._drivers[driver.driver_id] = driver

    def get_driver(self, driver_id: str) -> Driver | None:
        return self._drivers.get(driver_id)

    def all_drivers(self) -> list[Driver]:
        return list(self._drivers.values())
