from app.services.restaurant_service import RestaurantService, repo

service = RestaurantService()

def test_filter_by_food_item():
    # Ensure the restaurant is open for the test
    repo.df.loc[repo.df["restaurant_id"] == 1, "is_open"] = True
    # Test filtering by food item
    result = service.filter_items(1, food_item="Pizza")
    assert isinstance(result, list)