from app.services.restaurant_service import RestaurantService, repo

service = RestaurantService()

def test_add_favorite():

    result = service.favorite_restaurant(1)

    assert result == True