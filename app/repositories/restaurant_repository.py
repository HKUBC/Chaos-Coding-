import pandas as pd
import os

class RestaurantRepository:

    def __init__(self):

        current_dir = os.path.dirname(__file__)
        data_path = os.path.join(current_dir, "..", "data", "food_delivery.csv")

        self.df = pd.read_csv(data_path)

        if "is_open" not in self.df.columns:
            self.df["is_open"] = True


    def get_restaurant_ids(self):

        return self.df["restaurant_id"].unique()
    
    

    def restaurant_exists(self, restaurant_id):

        return restaurant_id in self.get_restaurant_ids()
    


    def get_open_restaurants(self):

        return self.df[self.df["is_open"] == True]
    


    def search_restaurants(self, cuisine):

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