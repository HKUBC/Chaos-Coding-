from app.model.menu import Menu
from app.model.restaurant import Restaurant
import pytest


def test_adding_second_menu_raises():
    restaurant = Restaurant(restaurant_id=2)
    first_menu = Menu(restaurant_id=2)
    restaurant.add_menu(first_menu)
    second_menu = Menu(restaurant_id=2)
    with pytest.raises(ValueError, match="already exists"):
        restaurant.add_menu(second_menu)
