from app.model.item import Item

def test_fooditem_creation(): 
    item = Item(1, "Burger", 5.99, 10)

    assert item.item_id == 1
    assert item.name == "Burger"
    assert item.price == 5.99
    assert item.quantity == 10