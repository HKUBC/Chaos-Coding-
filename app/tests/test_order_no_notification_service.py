from app.model.order import Order


def test_order_no_notification_service(data_service, item):
    o = Order(
        order_id="o99",
        customer_id="c99",
        restaurant_id="r1",
        data_service=data_service,
        notification_service=None,
    )
    o.add_item(item)
    o.start_order()
