from app.services.restaurant_service import RestaurantService, repo

service = RestaurantService()

def test_get_favorites():

    RestaurantService().favorite_restaurant(1)

    result = RestaurantService().get_favorites()

    assert isinstance(result, list)