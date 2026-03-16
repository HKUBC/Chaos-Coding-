from app.services.restaurant_service import RestaurantService, repo
service = RestaurantService()

def test_remove_favorite():

    service.favorite_restaurant(1)

    result = service.unfavorite_restaurant(1)

    assert result == True