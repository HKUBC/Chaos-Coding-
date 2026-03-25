from app.model.menu import Menu
from app.model.restaurant import Restaurant

#this test will check if a menu can be created after a restaurant is registered.
def test_menu_created_after_restaurant_registered():
    restaurant = Restaurant(restaurant_id=1)
    menu = Menu(restaurant_id=1)
    restaurant.add_menu(menu)

    assert restaurant.menu == menu
