import pytest
from app.model.notification import Notification, NotificationType
from app.repositories.notification_repository import NotificationRepository
from app.services.notification_service import NotificationService



@pytest.fixture
def repo():
    return NotificationRepository()


@pytest.fixture
def service(repo):
    return NotificationService(repo=repo)



def test_creates_with_valid_data():
    n = Notification(
        notification_id="n1",
        recipient_id="r42",
        recipient_type="restaurant",
        notification_type=NotificationType.ORDER_RECEIVED,
        message="New order received.",
    )
    assert n.notification_id == "n1"
    assert n.recipient_id == "r42"


def test_empty_message_raises_value_error():
    with pytest.raises(ValueError):
        Notification("n1", "r1", "restaurant", NotificationType.ORDER_RECEIVED, "")


def test_to_dict_contains_required_keys():
    n = Notification("n1", "r1", "restaurant", NotificationType.ORDER_RECEIVED, "msg")
    d = n.to_dict()
    for key in ("notification_id", "recipient_id", "recipient_type",
                "notification_type", "message", "metadata", "timestamp"):
        assert key in d


def test_metadata_defaults_to_empty_dict():
    n = Notification("n1", "r1", "restaurant", NotificationType.ORDER_RECEIVED, "msg")
    assert n.metadata == {}


def test_metadata_stored_correctly():
    n = Notification(
        "n1", "r1", "restaurant",
        NotificationType.ORDER_RECEIVED, "msg",
        metadata={"order_id": "o99"},
    )
    assert n.metadata["order_id"] == "o99"


def test_to_dict_notification_type_is_string():
    n = Notification("n1", "r1", "restaurant", NotificationType.ORDER_RECEIVED, "msg")
    assert isinstance(n.to_dict()["notification_type"], str)


def test_timestamp_is_set_on_creation():
    n = Notification("n1", "r1", "restaurant", NotificationType.ORDER_RECEIVED, "msg")
    assert n.timestamp is not None



def test_save_and_retrieve(repo):
    n = Notification("n1", "r1", "restaurant", NotificationType.ORDER_RECEIVED, "msg")
    repo.save(n)
    result = repo.get_for_recipient("r1")
    assert len(result) == 1


def test_returns_empty_list_for_unknown_recipient(repo):
    assert repo.get_for_recipient("nobody") == []


def test_multiple_notifications_same_recipient(repo):
    for i in range(3):
        n = Notification(str(i), "r1", "restaurant", NotificationType.ORDER_RECEIVED, "msg")
        repo.save(n)
    assert len(repo.get_for_recipient("r1")) == 3


def test_notifications_isolated_between_recipients(repo):
    n1 = Notification("n1", "r1", "restaurant", NotificationType.ORDER_RECEIVED, "msg")
    n2 = Notification("n2", "r2", "restaurant", NotificationType.ORDER_RECEIVED, "msg")
    repo.save(n1)
    repo.save(n2)
    assert len(repo.get_for_recipient("r1")) == 1
    assert len(repo.get_for_recipient("r2")) == 1


def test_clear_removes_all_notifications(repo):
    n = Notification("n1", "r1", "restaurant", NotificationType.ORDER_RECEIVED, "msg")
    repo.save(n)
    repo.clear()
    assert repo.get_for_recipient("r1") == []



def test_returns_notification_object(service):
    n = service.notify_restaurant_of_order("r42", "o1", "c5", 29.99)
    assert isinstance(n, Notification)


def test_notification_saved_to_repo(service, repo):
    service.notify_restaurant_of_order("r42", "o1", "c5", 29.99)
    assert len(repo.get_for_recipient("r42")) == 1


def test_notification_type_is_order_received(service):
    n = service.notify_restaurant_of_order("r42", "o1", "c5", 29.99)
    assert n.notification_type == NotificationType.ORDER_RECEIVED


def test_recipient_id_is_restaurant(service):
    n = service.notify_restaurant_of_order("r42", "o1", "c5", 29.99)
    assert n.recipient_id == "r42"


def test_recipient_type_is_restaurant(service):
    n = service.notify_restaurant_of_order("r42", "o1", "c5", 29.99)
    assert n.recipient_type == "restaurant"


def test_message_contains_order_id(service):
    n = service.notify_restaurant_of_order("r42", "order-XYZ", "c5", 29.99)
    assert "order-XYZ" in n.message


def test_message_contains_order_total(service):
    n = service.notify_restaurant_of_order("r42", "o1", "c5", 49.50)
    assert "49.50" in n.message


def test_metadata_contains_order_id(service):
    n = service.notify_restaurant_of_order("r42", "o1", "c5", 29.99)
    assert n.metadata["order_id"] == "o1"


def test_metadata_contains_customer_id(service):
    n = service.notify_restaurant_of_order("r42", "o1", "c5", 29.99)
    assert n.metadata["customer_id"] == "c5"


def test_metadata_contains_order_total(service):
    n = service.notify_restaurant_of_order("r42", "o1", "c5", 29.99)
    assert n.metadata["order_total"] == 29.99


def test_each_notification_has_unique_id(service):
    n1 = service.notify_restaurant_of_order("r42", "o1", "c5", 10.0)
    n2 = service.notify_restaurant_of_order("r42", "o2", "c5", 20.0)
    assert n1.notification_id != n2.notification_id


def test_get_notifications_returns_list_of_dicts(service):
    service.notify_restaurant_of_order("r42", "o1", "c5", 29.99)
    result = service.get_notifications("r42")
    assert isinstance(result[0], dict)