def test_order_start_triggers_notification(order, repo, item):
    order.add_item(item)
    order.start_order()
    assert len(repo.get_for_recipient("c1")) == 1
