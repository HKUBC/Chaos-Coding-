import os
import pandas as pd
from app.model.customer import Customer
from app.model.restaurant_owner import RestaurantOwner
from app.model.driver import Driver

# This repository manages all user-related data, including customers, restaurant owners, and drivers.

class UserRepository:
    def __init__(self, df: pd.DataFrame | None = None):
        self._customers: dict[str, Customer] = {}
        self._owners: dict[str, RestaurantOwner] = {}
        self._drivers: dict[str, Driver] = {}

        if df is None:
            current_dir = os.path.dirname(__file__)
            csv_path = os.path.join(current_dir, "..", "data", "food_delivery.csv")
            df = pd.read_csv(csv_path)

        self._load_from_df(df)

    def _load_from_df(self, df: pd.DataFrame):
        # create one customer per unique customer_id
        for _, row in df.drop_duplicates(subset="customer_id").iterrows():
            self._customers[row["customer_id"]] = Customer(
                customer_id=row["customer_id"],
                age=int(row["age"]),
                gender=row["gender"],
                location=row["location"],
            )

        # create one restaurant owner per unique restaurant_id
        for restaurant_id in df["restaurant_id"].unique():
            restaurant_id = str(restaurant_id)
            owner_id = f"owner_{restaurant_id}"
            self._owners[owner_id] = RestaurantOwner(
                owner_id=owner_id,
                restaurant_id=restaurant_id,
            )

    def add_customer(self, customer: Customer):
        if customer.customer_id in self._customers:
            raise ValueError(f"Customer {customer.customer_id} already exists.")
        self._customers[customer.customer_id] = customer

    def add_owner(self, owner: RestaurantOwner):
        if owner.owner_id in self._owners:
            raise ValueError(f"Restaurant owner {owner.owner_id} already exists.")
        self._owners[owner.owner_id] = owner

    def add_driver(self, driver: Driver):
        if driver.driver_id in self._drivers:
            raise ValueError(f"Driver {driver.driver_id} already exists.")
        self._drivers[driver.driver_id] = driver

    def get_customer(self, customer_id: str) -> Customer | None:
        return self._customers.get(customer_id)

    def get_owner_by_restaurant(self, restaurant_id: str) -> RestaurantOwner | None:
        owner_id = f"owner_{restaurant_id}"
        return self._owners.get(owner_id)

    def get_driver(self, driver_id: str) -> Driver | None:
        return self._drivers.get(driver_id)

    def all_customers(self) -> list[Customer]:
        return list(self._customers.values())

    def all_owners(self) -> list[RestaurantOwner]:
        return list(self._owners.values())

    def all_drivers(self) -> list[Driver]:
        return list(self._drivers.values())
