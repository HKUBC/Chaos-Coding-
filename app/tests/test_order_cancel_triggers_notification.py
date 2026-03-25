def test_order_cancel_triggers_notification(order, repo, item):
    order.add_item(item)
    order.start_order()
    repo.clear()
    order.cancel_order()
    assert len(repo.get_for_recipient("c1")) == 1
