from app.model.restaurant import Restaurant
from app.model.menu import Menu


def test_menu_require_restaurant():
    restaurant = Restaurant(1)
    menu = Menu(restaurant.restaurant_id)

    assert menu.restaurant_id == restaurant.restaurant_id
