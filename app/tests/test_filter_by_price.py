from app.services.restaurant_service import RestaurantService, repo

service = RestaurantService()




def test_filter_by_price(): 
    # Ensure the restaurant is open for the test
    repo.df.loc[repo.df["restaurant_id"] == 1, "is_open"] = True
    # Test filtering by price range
    result = service.filter_items(1, min_price=10, max_price=20)
    # Ensure the result is a list
    assert isinstance(result, list)
