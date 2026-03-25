def test_order_cancelled_message_has_order_id(order, repo, item):
    order.add_item(item)
    order.start_order()
    order.cancel_order()
    notifications = repo.get_for_recipient("c1")
    cancelled = next(
        n for n in notifications if n.metadata["new_status"] == "cancelled"
    )
    assert "o1" in cancelled.message
