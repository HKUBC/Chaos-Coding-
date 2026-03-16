import pandas as pd
import os

class RestaurantRepository:

    def __init__(self):

        current_dir = os.path.dirname(__file__)
        data_path = os.path.join(current_dir, "..", "data", "food_delivery.csv")

        self.df = pd.read_csv(data_path)

        if "is_open" not in self.df.columns:
            self.df["is_open"] = True
        
        self.favorites = set()  # this will store the restaurant ids of the user's favorite restaurants, it is a set to avoid duplicates



    def get_all_restaurants(self): #returns a list of all the restaurants in the dataframe
        return self.df["restaurant_id"].unique().tolist()

    def get_restaurant_ids(self): #returns a list of unique restaurant ids from the dataframe
        return self.df["restaurant_id"].unique()
    
    def restaurant_exists(self, restaurant_id): #returns true if the restaurant id exists in the dataframe, false otherwise
        return restaurant_id in self.get_restaurant_ids()
    

    def get_open_restaurants(self): # this function gives out only the restaurant that are open
     return self.df[self.df["is_open"] == True]
    


    def search_restaurants(self, cuisine): #returns restaurant that has the cuisine
        return self.df[
            self.df["preferred_cuisine"].str.contains(
                cuisine,
                case=False
            )
        ]



    def filter_menu(self, restaurant_id, cuisine=None):

        data = self.df[self.df["restaurant_id"] == restaurant_id]

        if cuisine:
            data = data[
                data["preferred_cuisine"].str.contains(
                    cuisine,
                    case=False
                )
            ]

        return data[["food_item","order_value","preferred_cuisine"]]
    
    
    
    def get_restaurant_by_id(self, restaurant_id):

        data = self.df[self.df["restaurant_id"] == restaurant_id]

        if data.empty:
            return None

        return data.iloc[0].to_dict()
    

    def restaurant_is_open(self, restaurant_id):

        restaurant = self.df[self.df["restaurant_id"] == restaurant_id]

        if restaurant.empty:
            return False

        return restaurant["is_open"].iloc[0] == True
    


    def add_favorite(self, restaurant_id): 
        #adds a restaurant to the user's favorites list, returns true if the restaurant was added successfully, false if the restaurant id does not exist in the dataframe

        if restaurant_id not in self.get_restaurant_ids():
            return False

        self.favorites.add(restaurant_id)
        return True


    def remove_favorite(self, restaurant_id):
        #removes a restaurant from the user's favorites list, returns true if the restaurant was removed successfully, false if the restaurant id does not exist in the favorites list
      
        if restaurant_id in self.favorites:
            self.favorites.remove(restaurant_id)
            return True

        return False


    def get_favorites(self):
        #returns a list of the user's favorite restaurants, it is a list to maintain the order of the favorites
        return list(self.favorites)




    def filter_menu(
        self,
        restaurant_id,
        food_item=None,
        cuisine=None,
        order_time=None,
        min_price=None,
        max_price=None
    ):

        data = self.df[self.df["restaurant_id"] == restaurant_id]

        if food_item:
            data = data[data["food_item"].str.contains(food_item, case=False)]

        if cuisine:
            data = data[data["preferred_cuisine"].str.contains(cuisine, case=False)]

        if order_time:
            data = data[data["order_time"].str.contains(order_time, case=False)]

        if min_price is not None:
            data = data[data["order_value"] >= min_price]

        if max_price is not None:
            data = data[data["order_value"] <= max_price]

        return data[["food_item", "order_value", "preferred_cuisine", "order_time"]]
