from app.repositories.restaurant_repository import RestaurantRepository

repo = RestaurantRepository()

class RestaurantService:

    def get_all_restaurants(self):
        return repo.get_all_restaurants()

    def get_restaurant(self, restaurant_id):

        if not repo.restaurant_exists(restaurant_id):
            return None

        if not repo.restaurant_is_open(restaurant_id):
            return None

        return repo.get_restaurant_by_id(restaurant_id)
    


    def get_open_restaurants(self):

        data = repo.get_open_restaurants()

        return data[["restaurant_id"]].drop_duplicates().to_dict("records")
    


    def search_restaurants(self, cuisine):

        data = repo.search_restaurants(cuisine)

        data = data[data["is_open"] == True]

        return data[
            ["restaurant_id","food_item","preferred_cuisine"]
        ].to_dict("records")
    
    

    def get_menu(self, restaurant_id, cuisine=None):
        return self.filter_menu(restaurant_id, cuisine)

    def filter_menu(self, restaurant_id, cuisine=None):

        if not repo.restaurant_exists(restaurant_id):
            return None

        if not repo.restaurant_is_open(restaurant_id):
            return None

        data = repo.filter_menu(restaurant_id, cuisine)

        return data.to_dict("records")
    

    def favorite_restaurant(self, restaurant_id): 
        #adds the restaurant to the user's favorites, it checks if the restaurant exists and is open before adding it to the favorites    

        if not repo.restaurant_exists(restaurant_id):
            return False

        return repo.add_favorite(restaurant_id)
    


    def unfavorite_restaurant(self, restaurant_id):
        #removes the restaurant from the user's favorites, it checks if the restaurant exists before removing it from the favorites
        return repo.remove_favorite(restaurant_id)


    def get_favorites(self):
        #returns a list of the user's favorite restaurants, it checks if the restaurant is open before returning it in the list
        favorites = repo.get_favorites()

        results = []

        for rid in favorites:
            restaurant = repo.get_restaurant_by_id(rid)
            if restaurant:
                results.append(restaurant)

        return results
    


    def toggle_item_availability(self, restaurant_id: int, food_item: str) -> bool:
        return repo.toggle_item_availability(restaurant_id, food_item)

    def get_unavailable_items(self, restaurant_id: int) -> list:
        return repo.get_unavailable_items(restaurant_id)

    def add_item(self, restaurant_id: int, food_item: str, cuisine: str, price: float) -> None:
        repo.add_item(restaurant_id, food_item, cuisine, price)

    def archive_item(self, restaurant_id: int, food_item: str) -> bool:
        return repo.archive_item(restaurant_id, food_item)

    def filter_items(
        self,
        restaurant_id,
        food_item=None,
        cuisine=None,
        order_time=None,
        min_price=None,
        max_price=None
    ):

        if not repo.restaurant_exists(restaurant_id):
            return None

        if not repo.restaurant_is_open(restaurant_id):
            return None

        data = repo.filter_menu(
            restaurant_id,
            food_item,
            cuisine,
            order_time,
            min_price,
            max_price
        )

        return data.to_dict("records")
    