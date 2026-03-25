from app.model.user_role import UserRole


class Driver:
    def __init__(self, driver_id: str, name: str):
        self.driver_id = driver_id
        self.name      = name
        self.role      = UserRole.DRIVER
