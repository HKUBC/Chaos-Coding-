class Restaurant:
    def __init__(self, restaurant_id,): #takes in the restaurant id as a parameter and initializes the restaurant object with an empty menu
        self.restaurant_id = restaurant_id 
        self.menu = []


    def add_menu(self, menu):
      self.menu.append(menu)
