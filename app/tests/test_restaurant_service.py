from app.services.restaurant_service import RestaurantService, repo

service = RestaurantService()


def test_restaurant_exists():

    result = service.get_restaurant(1)

    assert result is not None



def test_restaurant_does_not_exist():

    result = service.get_restaurant(999999)

    assert result is None




def test_get_existing_restaurant():

    repo.df.loc[repo.df["restaurant_id"] == 1, "is_open"] = True
   
    result = service.get_restaurant(1)

    assert result is not None
   
    assert result["restaurant_id"] == 1



def test_get_nonexistent_restaurant():
   
    result = service.get_restaurant(999999)
   
    assert result is None



def test_open_restaurant_is_returned():

    repo.df.loc[repo.df["restaurant_id"] == 1, "is_open"] = True

    result = service.get_restaurant(1)

    assert result is not None



def test_get_open_restaurants():

    result = service.get_open_restaurants()

    assert isinstance(result, list)



def test_closed_restaurant_not_returned():

    original_value = repo.df.loc[repo.df["restaurant_id"] == 1, "is_open"].iloc[0]

    repo.df.loc[repo.df["restaurant_id"] == 1, "is_open"] = False

    result = service.get_restaurant(1)

    assert result is None

    repo.df.loc[repo.df["restaurant_id"] == 1, "is_open"] = original_value



def test_search_by_cuisine():

    result = service.search_restaurants(cuisine="Indian")

    assert isinstance(result, list)



def test_filter_menu():

    # make sure restaurant 1 is open
    repo.df.loc[repo.df["restaurant_id"] == 1, "is_open"] = True

    result = service.filter_menu(1)

    assert isinstance(result, list)



def test_filter_menu_with_cuisine():

    repo.df.loc[repo.df["restaurant_id"] == 1, "is_open"] = True

    result = service.filter_menu(1, cuisine="Indian")

    assert isinstance(result, list)



def test_filter_menu_closed_restaurant():

    original_value = repo.df.loc[repo.df["restaurant_id"] == 1, "is_open"].iloc[0]

    repo.df.loc[repo.df["restaurant_id"] == 1, "is_open"] = False

    result = service.filter_menu(1)

    assert result is None

    repo.df.loc[repo.df["restaurant_id"] == 1, "is_open"] = original_value