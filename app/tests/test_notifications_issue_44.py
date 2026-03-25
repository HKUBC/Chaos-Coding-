import pytest
from unittest.mock import MagicMock
from app.model.notification import Notification, NotificationType
from app.model.order import Order
from app.model.order_status import OrderStatus
from app.repositories.notification_repository import NotificationRepository
from app.services.notification_service import NotificationService


@pytest.fixture
def repo():
    return NotificationRepository()


@pytest.fixture
def service(repo):
    return NotificationService(repo=repo)


@pytest.fixture
def mock_data_service():
    svc = MagicMock()
    svc.load_data.return_value = [
        {"delivery_time": "30 mins"},
        {"delivery_time": "45 mins"},
    ]
    return svc


@pytest.fixture
def order(mock_data_service, service):
    return Order(
        order_id="o1",
        customer_id="c1",
        restaurant_id="r1",
        data_service=mock_data_service,
        notification_service=service,
    )



def test_returns_notification_object(service):
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


def test_metadata_contains_order_id(service):
    n = service.notify_user_of_order_status("c1", "o1", "pending")
    assert n.metadata["order_id"] == "o1"


def test_metadata_contains_new_status(service):
    n = service.notify_user_of_order_status("c1", "o1", "preparing")
    assert n.metadata["new_status"] == "preparing"


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



def test_update_status_triggers_notification(order, repo):
    order.update_status(OrderStatus.PENDING)
    assert len(repo.get_for_recipient("c1")) == 1


def test_start_order_triggers_notification(order, mock_data_service):
    from app.model.item import Item
    order.add_item(Item(item_id=1, name="Burger", price=9.99))
    order.start_order()
    notifications = order._notification_service.get_notifications("c1")
    assert len(notifications) == 1


def test_cancel_order_triggers_notification(order, repo):
    from app.model.item import Item
    order.add_item(Item(item_id=1, name="Burger", price=9.99))
    order.start_order()
    repo.clear()  # clear the pending notification first
    order.cancel_order()
    assert len(repo.get_for_recipient("c1")) == 1


def test_notification_without_service_does_not_crash(mock_data_service):
    from app.model.item import Item
    o = Order(
        order_id="o99",
        customer_id="c99",
        restaurant_id="r1",
        data_service=mock_data_service,
        notification_service=None,
    )
    o.add_item(Item(item_id=1, name="Burger", price=9.99))
    o.start_order()  # should not raise even with no notification service


def test_cancelled_notification_message_contains_order_id(order, repo):
    from app.model.item import Item
    order.add_item(Item(item_id=1, name="Burger", price=9.99))
    order.start_order()
    order.cancel_order()
    notifications = repo.get_for_recipient("c1")
    cancelled_notification = next(
        n for n in notifications if n.metadata["new_status"] == "cancelled"
    )
    assert "o1" in cancelled_notification.message