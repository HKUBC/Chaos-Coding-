import pandas as pd
from app.model.restaurant import Restaurant
from app.model.menu import Menu
from app.model.item import Item

def load_restaurant(file_path):
    df = pd.read_csv(file_path)
    restaurants = {}

    for _, row in df.iterrows():
        restaurant_id = row['restaurant_id'] #gets the restaurant id from the csv file
        #if there is no restaurant with the id, then create a new restaurant and add it to the dictionary
        if restaurant_id not in restaurants:
            restaurants[restaurant_id] = Restaurant(restaurant_id)
        
        restaurant = restaurants[restaurant_id] #gets the restaurant object from the dictionary, this is for a specific restaurant id
        
        #now checking if the menu exists for the restaurant, if not create a new menu and add it to the restaurant
        if not restaurant.menu:
            menu = Menu(restaurant_id)
            restaurant.add_menu(menu)
        else:
            menu = restaurant.menu[0] #gets the menu object from the restaurant, this is for a specific restaurant id

        #now we create an item object and add it to the menu
        item = Item(row['item_id'], row['name'], row['price'], row['quantity'])
        menu.add_item(item)

    return restaurants