from app.services.notification_service import NotificationService

notification_service = NotificationService()














# After payment confirmed:
notification_service.notify_restaurant_of_order(
    restaurant_id=order.restaurant_id,
    order_id=order.order_id,
    customer_id=order.customer_id,
    order_total=order.order_total(),
)