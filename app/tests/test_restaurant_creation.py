from app.model.restaurant import Restaurant

def test_restaurant_creation():
  r = Restaurant(1)

  assert r.restaurant_id == 1
  assert r.menu == []
