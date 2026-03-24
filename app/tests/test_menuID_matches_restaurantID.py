import app.model.restaurant as Restaurant
import app.model.menu as Menu

def test_menuID_matches_restaurantID():
    restaurant = Restaurant.Restaurant(restaurant_id=1)
    menu = Menu.Menu(restaurant_id=1)
    restaurant.add_menu(menu)

    assert menu.restaurant_id == restaurant.restaurant_id