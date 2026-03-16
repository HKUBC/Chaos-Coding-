from app.services.restaurant_service import RestaurantService, repo

service = RestaurantService()

def test_get_favorites():

    service.favorite_restaurant(1)

    result = service.get_favorites()

    assert isinstance(result, list)