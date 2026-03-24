import pandas as pd
from app.model.restaurant import Restaurant
from app.model.menu import Menu
from app.model.item import Item

def load_all_restaurant(file_path):
    df = pd.read_csv(file_path)
    restaurants_registry = {}

    grouped = df.groupby('restaurant_id') # created this to group the data by restraunt id so we can process them one by one\\

    for res_id, group in grouped:

        new_restaurant = Restaurant(restaurant_id=res_id) # create a new restaurant object for each restaurant id

        new_menu = Menu(restaurant_id=res_id) # create a new menu object for each restaurant id

        for _, row in group.iterrows(): # iterate through the rows of the group, which is the data for a specific restaurant id

            new_item = Item(
                item_id=row['order_id'],
                name=row['food_item'],
                price=float(row['order_value']),
                quantity=1
            ) # create a new item object for each row of the group, which is the data for a specific restaurant id

            new_menu.add_item(new_item) # add the item to the menu
            
        new_restaurant.add_menu(new_menu) # add the menu to the restaurant
        restaurants_registry[res_id] = new_restaurant # add the restaurant to the registry

    return restaurants_registry

  