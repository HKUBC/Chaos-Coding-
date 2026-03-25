import os
import pytest
from app.model.item import Item
from app.model.notification import Notification, NotificationType
from app.model.order import Order
from app.model.order_status import OrderStatus
from app.repositories.notification_repository import NotificationRepository
from app.services.notification_service import NotificationService
from app.services.csv_service import CSVService


@pytest.fixture
def repo():
    return NotificationRepository()


@pytest.fixture
def service(repo):
    return NotificationService(repo=repo)


@pytest.fixture
def data_service():
    current_dir = os.path.dirname(__file__)
    csv_path = os.path.join(current_dir, "..", "data", "food_delivery.csv")
    return CSVService(csv_path)


@pytest.fixture
def order(data_service, service):
    return Order(
        order_id="o1",
        customer_id="c1",
        restaurant_id="r1",
        data_service=data_service,
        notification_service=service,
    )


@pytest.fixture
def item():
    return Item(item_id=1, name="Burger", price=9.99)



    n = service.notify_user_of_order_status("c1", "o1", "pending")
    assert isinstance(n, Notification)


def test_recipient_is_customer(service):
    n = service.notify_user_of_order_status("c1", "o1", "pending")
    assert n.recipient_id == "c1"
    assert n.recipient_type == "customer"


def test_notification_type_is_order_status(service):
    n = service.notify_user_of_order_status("c1", "o1", "pending")
    assert n.notification_type == NotificationType.ORDER_STATUS


def test_pending_status_message(service):
    n = service.notify_user_of_order_status("c1", "o1", "pending")
    assert "pending" in n.message.lower()


def test_preparing_status_message(service):
    n = service.notify_user_of_order_status("c1", "o1", "preparing")
    assert "prepared" in n.message.lower()


def test_delivered_status_message(service):
    n = service.notify_user_of_order_status("c1", "o1", "delivered")
    assert "delivered" in n.message.lower()


def test_cancelled_status_message(service):
    n = service.notify_user_of_order_status("c1", "o1", "cancelled")
    assert "cancelled" in n.message.lower()


def test_unknown_status_still_sends_notification(service):
    n = service.notify_user_of_order_status("c1", "o1", "unknown_status")
    assert "unknown_status" in n.message.lower()


def test_message_contains_order_id(service):
    n = service.notify_user_of_order_status("c1", "order-ABC", "pending")
    assert "order-ABC" in n.message


def test_message_contains_order_id_in_pending(service):
    n = service.notify_user_of_order_status("c1", "o1", "pending")
    assert "o1" in n.message


def test_notification_saved_to_repo(service, repo):
    service.notify_user_of_order_status("c1", "o1", "pending")
    assert len(repo.get_for_recipient("c1")) == 1


def test_multiple_status_updates_all_saved(service, repo):
    service.notify_user_of_order_status("c1", "o1", "pending")
    service.notify_user_of_order_status("c1", "o1", "preparing")
    service.notify_user_of_order_status("c1", "o1", "delivered")
    assert len(repo.get_for_recipient("c1")) == 3


def test_each_notification_has_unique_id(service):
    n1 = service.notify_user_of_order_status("c1", "o1", "pending")
    n2 = service.notify_user_of_order_status("c1", "o1", "preparing")
    assert n1.notification_id != n2.notification_id


def test_different_customers_get_separate_notifications(service, repo):
    service.notify_user_of_order_status("c1", "o1", "pending")
    service.notify_user_of_order_status("c2", "o2", "pending")
    assert len(repo.get_for_recipient("c1")) == 1
    assert len(repo.get_for_recipient("c2")) == 1



    assert len(repo.get_for_recipient("c1")) == 1


def test_start_order_triggers_notification(order, repo, item):
    order.add_item(item)
    order.start_order()
    assert len(repo.get_for_recipient("c1")) == 1


def test_cancel_order_triggers_notification(order, repo, item):
    order.add_item(item)
    order.start_order()
    repo.clear()
    order.cancel_order()
    assert len(repo.get_for_recipient("c1")) == 1


def test_notification_without_service_does_not_crash(data_service, item):
    o = Order(
        order_id="o99",
        customer_id="c99",
        restaurant_id="r1",
        data_service=data_service,
        notification_service=None,
    )
    o.add_item(item)
    o.start_order()


def test_preparing_status_notification_saved(order, repo):
    order.update_status(OrderStatus.PREPARING)
    notifications = repo.get_for_recipient("c1")
    assert any("prepared" in n.message.lower() for n in notifications)


def test_delivered_status_notification_saved(order, repo):
    order.update_status(OrderStatus.DELIVERED)
    notifications = repo.get_for_recipient("c1")
    assert any("delivered" in n.message.lower() for n in notifications)


def test_cancelled_notification_message_contains_order_id(order, repo, item):
    order.add_item(item)
    order.start_order()
    order.cancel_order()
    notifications = repo.get_for_recipient("c1")
    cancelled = next(
        n for n in notifications if "cancelled" in n.message.lower()
    )
    assert "o1" in cancelled.message
