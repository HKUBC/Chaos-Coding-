import os
import pytest
from app.model.item import Item
from app.model.order import Order
from app.repositories.notification_repository import NotificationRepository
from app.services.notification_service import NotificationService
from app.services.csv_service import CSVService
import app.services.auth_service as auth_module


@pytest.fixture(autouse=True)
def isolate_auth_data(tmp_path, monkeypatch):
    """Redirect the auth data file to a temp dir for every test so usernames never conflict."""
    monkeypatch.setattr(auth_module, '_DATA_FILE', str(tmp_path / 'users.json'))


@pytest.fixture
def repo():
    return NotificationRepository()


@pytest.fixture
def service(repo):
    return NotificationService(repo=repo)


@pytest.fixture
def data_service():
    current_dir = os.path.dirname(__file__)
    csv_path = os.path.join(current_dir, "..", "..", "data", "food_delivery.csv")
    return CSVService(csv_path)


@pytest.fixture
def order(data_service, service):
    return Order(
        order_id="o1",
        customer_id="c1",
        restaurant_id="r1",
        notification_service=service,
    )


@pytest.fixture
def item():
    return Item(item_id=1, name="Burger", price=9.99)


