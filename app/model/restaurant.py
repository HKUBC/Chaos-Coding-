from app.model import menu
from app.model.restaurant_registry import Restaurant_registry


class Restaurant:
    def __init__(self, restaurant_id): #takes in the restaurant id as a parameter and initializes the restaurant object with an empty menu
        self.restaurant_id = restaurant_id 
        Restaurant_registry.register_restaurant(restaurant_id) # this will register the restaurant id in the restaurant registry
        self.menu = None #this is the menu for the restaurant
        
        #self.menu = menu if menu is not None else []
        #self.menu = []

    def add_menu(self, menu):
      if self.menu is not None: #if the restaurant already has a menu, then raise an error because a restaurant can only have one menu
          raise ValueError("Menu already exists for this restaurant.")

      self.menu = menu #sets the menu for the restaurant
      

