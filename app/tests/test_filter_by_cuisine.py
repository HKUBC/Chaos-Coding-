from app.services.restaurant_service import RestaurantService, repo

service = RestaurantService()


def test_filter_by_cuisine():
    # Ensure the restaurant is open for the test
    repo.df.loc[repo.df["restaurant_id"] == 1, "is_open"] = True
    # Test filtering by cuisine
    result = service.filter_items(1, cuisine="Indian")
    # Ensure the result is a list
    assert isinstance(result, list)
