class restaurantRepository:
    def __init__(self):
        self.restaurants = {}

    def get_restaurant_id(self, restaurant_id):
        return 
    
    def add_restaurant(self, restaurant):
        self.restaurants[restaurant.restaurant_id] = restaurant
    
    def get_restaurant(self, restaurant_id):
        return self.restaurants.get(restaurant_id)