from app.services.restaurant_service import RestaurantService

service = RestaurantService()


def test_restaurant_exists():

    result = service.get_restaurant(1)

    assert result is not None


def test_restaurant_does_not_exist():

    result = service.get_restaurant(999999)

    assert result is None