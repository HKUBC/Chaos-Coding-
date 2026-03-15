from app.repositories.restaurant_repository import RestaurantRepository

repo = RestaurantRepository()

class RestaurantService:

    def get_restaurant(self, restaurant_id):

        if not repo.restaurant_exists(restaurant_id):
            return None

        return repo.get_restaurant_by_id(restaurant_id)
    


    def get_open_restaurants(self):

        data = repo.get_open_restaurants()

        return data[["restaurant_id"]].drop_duplicates().to_dict("records")
    


    def search_restaurants(self, cuisine):

        data = repo.search_restaurants(cuisine)

        return data[
            ["restaurant_id","food_item","preferred_cuisine"]
        ].to_dict("records")
    
    

    def filter_menu(self, restaurant_id, cuisine=None):

        if not repo.restaurant_exists(restaurant_id):
            return None

        data = repo.filter_menu(restaurant_id, cuisine)

        return data.to_dict("records")