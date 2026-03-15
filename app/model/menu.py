class Menu:
    def __init__(self, restaurant_id):
        if restaurant_id is None:
            raise ValueError("Restaurant ID cannot be None.")
        
        self.restaurant_id = restaurant_id
        self.items = [] #these are the food items

    def add_item(self, item):
        self.items.append(item)
      
    
        