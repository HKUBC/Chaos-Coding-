from app.model.restaurant_registry import Restaurant_registry
from app.services.notification_service import NotificationService


class Menu:
    def __init__(self, restaurant_id):
        if restaurant_id is None:
            raise ValueError("Restaurant ID cannot be None.")
        
        if not Restaurant_registry .is_registered(restaurant_id): # this will check if the restaurant id is registered in the restaurant registry
            raise ValueError("Restaurant ID is not registered.")
        
        self.restaurant_id = restaurant_id
        self.items = [] #these are the food items
        # We will use the notification service to send notifications 
        self._notification_service = NotificationService()

    def add_item(self, item): #takes in an item object and adds it to the menu, also checks if the price and quantity of the item are valid

        if item.price < 0:
            raise ValueError("Item price cannot be negative.")
        if item.quantity < 0:
            raise ValueError("Item quantity cannot be negative.")
        
        item.restaurant_id = self.restaurant_id # this will stamp the restaurant id of the item to the restaurant id of the menu, this is important for when we want to retrieve the items for a specific restaurant

        self._notification_service.notify_users_of_menu_update(
            restaurant_id=self.restaurant_id,
             item_name=item.name,
        )
        self.items.append(item)

    def get_all_items(self):
        return self.items
    
    def get_item_by_id(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                return item
    

      
    
        