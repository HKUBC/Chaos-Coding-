from app.model.user_role import UserRole


class RestaurantOwner:
    def __init__(self, owner_id: str, restaurant_id: str):
        self.owner_id      = owner_id
        self.restaurant_id = restaurant_id
        self.role          = UserRole.RESTAURANT_OWNER
