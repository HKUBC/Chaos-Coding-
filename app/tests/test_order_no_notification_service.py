from app.model.order import Order


def test_order_no_notification_service(item):
    o = Order(
        order_id="o99",
        customer_id="c99",
        restaurant_id="r1",
        notification_service=None,
    )
    o.add_item(item)
    o.start_order()
