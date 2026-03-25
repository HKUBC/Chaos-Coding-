class Restaurant_registry:
  _registered_ids : set = set() # this will keep track of all the registered restaurant ids, this is important for when we want to retrieve the menu for a specific restaurant

  @classmethod # using class method because we want to access the class variable _registered_ids
  def register_restaurant(cls, restaurant_id: int):
     cls._registered_ids.add(restaurant_id) #this will add the restaurant id to the set of registered ids

  @classmethod
  def is_registered(cls, restaurant_id: int) -> bool:
     return restaurant_id in cls._registered_ids # this will check if the restaurant id is in the set of registered ids, if it is then it will return true, otherwise it will return false
  
  @classmethod
  def get_registered_ids(cls):
     return list(cls._registered_ids) # this will return the list of registered ids, this is important for when we want to retrieve the menu for a specific restaurant