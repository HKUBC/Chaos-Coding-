from app.model.item import Item

def test_fooditem_negative_price():
    try:
        item = Item(1, "Burger", -5.99, 10)
        assert False, "Expected ValueError for negative price"
    except ValueError as e:
        assert str(e) == "Price cannot be negative."