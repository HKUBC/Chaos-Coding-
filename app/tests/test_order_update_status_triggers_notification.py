from app.model.order_status import OrderStatus


def test_order_update_status_triggers_notification(order, repo):
    order.update_status(OrderStatus.PENDING)
    assert len(repo.get_for_recipient("c1")) == 1
