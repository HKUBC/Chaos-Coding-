from app.model.restaurant import Restaurant
from app.model.menu import Menu

def test_two_restaurant_have_different_menus():
  r1 = Restaurant(restaurant_id=1)
  r2 = Restaurant(restaurant_id=2)
  m1 = Menu(restaurant_id=1)
  m2 = Menu(restaurant_id=2)
  r1.add_menu(m1)
  r2.add_menu(m2)
  assert r1.menu != r2.menu
  assert r1.menu is m1
  assert r2.menu is m2
