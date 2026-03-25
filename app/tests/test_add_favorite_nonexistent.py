from app.services.restaurant_service import RestaurantService, repo

service = RestaurantService()

def test_add_favorite_nonexistent():

    result = RestaurantService().favorite_restaurant(999999)

    assert result == False