from app.services.restaurant_service import RestaurantService, repo
service = RestaurantService()

def test_remove_favorite():

    RestaurantService().favorite_restaurant(1)

    result = RestaurantService().unfavorite_restaurant(1)

    assert result == True