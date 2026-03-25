from app.model.restaurant import Restaurant
from app.model.menu import Menu
from app.model.item import Item


def test_items_from_different_restaurants_have_different_ids():
    Restaurant(restaurant_id=20)
    Restaurant(restaurant_id=30)
    menu1 = Menu(restaurant_id=20)
    menu2 = Menu(restaurant_id=30)

    item1 = Item(item_id=1, name="Burger", price=9.99)
    item2 = Item(item_id=2, name="Pizza", price=12.99)

    menu1.add_item(item1)
    menu2.add_item(item2)

    assert item1.restaurant_id == 20
    assert item2.restaurant_id == 30
    assert item1.restaurant_id != item2.restaurant_id
