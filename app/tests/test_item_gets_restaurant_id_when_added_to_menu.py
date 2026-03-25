from app.model.restaurant import Restaurant
from app.model.menu import Menu
from app.model.item import Item


def test_item_gets_restaurant_id_when_added_to_menu():
    restaurant = Restaurant(restaurant_id=10)
    menu = Menu(restaurant_id=10)
    item = Item(item_id=1, name="Burger", price=9.99)

    menu.add_item(item)

    assert item.restaurant_id == 10
