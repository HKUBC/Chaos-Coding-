from app.model.restaurant import Restaurant

def test_menu_without_restaurant():
    restaurant = Restaurant(1)

    assert restaurant.restaurant_id == 1
    assert restaurant.menu == []