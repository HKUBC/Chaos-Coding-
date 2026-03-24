from app.model.item import Item


def test_item_has_no_restaurant_id_before_added():
    item = Item(item_id=1, name="Burger", price=9.99)

    assert item.restaurant_id is None
