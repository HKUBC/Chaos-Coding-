class Restaurant:
    def __init__(self, restaurant_id): #takes in the restaurant id as a parameter and initializes the restaurant object with an empty menu
        self.restaurant_id = restaurant_id 
        self.menu = None #this is the menu for the restaurant



    def add_menu(self, menu):
      if self.menu is not None: #if the restaurant already has a menu, then raise an error because a restaurant can only have one menu
          raise ValueError("Menu already exists for this restaurant.")

      self.menu = menu #sets the menu for the restaurant

