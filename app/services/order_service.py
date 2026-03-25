from app.model.order import Order
from app.model.order_status import OrderStatus
from app.repositories.order_repository import OrderRepository


repo = OrderRepository()

class OrderService:

    # Creates a new order by using an order_id, customer_id, and restaurant_id
    def create_order(self, order_id: str, customer_id: str, restaurant_id: str) -> Order:
        order = Order(order_id, customer_id, restaurant_id)
        return order
    # Starts an order by changing its status to pending and saving it to the session storage
    def place_order(self, order: Order) -> Order:
        order.start_order()
        repo.save(order)
        return order

    # Retrieves an order by its order_id
    def get_order(self, order_id: str) -> Order | None:
        return repo.get_order_by_id(order_id)
    
    # Retrieves all orders associated with a specific customer_id
    def get_orders_by_customer(self, customer_id: str) -> list[Order] | None:
        return repo.get_orders_by_customer(customer_id)
    

# Retrieves all orders associated with a specific customer_id from the session storage and formats them for output
    def get_order_history(self, customer_id: str) -> list[dict]:
        orders = repo.get_session_orders(customer_id)
        return [
            {
                "order_id":      o.order_id,
                "restaurant_id": o.restaurant_id,
                "status":        o.status.value,
                "total":         o.order_total(),
                "items": [
                    {
                        "item_id":  i.item_id,
                        "name":     i.name,
                        "price":    i.price,
                        "quantity": i.quantity,
                    }
                    for i in o.items
                ],
            }
            for o in orders
        ]

# Allows customers to reorder a past order by creating a new order with the same items and restaurant, but a new order_id
    def reorder(self, customer_id: str, order_id: str, new_order_id: str) -> Order:
        all_orders = repo.get_session_orders(customer_id)
        past_order = next((o for o in all_orders if o.order_id == order_id), None)

        if past_order is None:
            raise ValueError(f"Order #{order_id} not found.")

        if past_order.customer_id != customer_id:
            raise ValueError("You can only reorder your own past orders.")

        from app.model.item import Item
        new_order = Order(new_order_id, customer_id, past_order.restaurant_id)

        for item in past_order.items:
            new_item = Item(
                item_id=item.item_id,
                name=item.name,
                price=item.price,
                quantity=item.quantity,
            )
            new_order.add_item(new_item)

        new_order.start_order()
        repo.save(new_order)
        return new_order