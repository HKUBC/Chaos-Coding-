from app.model.user_role import UserRole


class Customer:
    def __init__(self, customer_id: str, age: int, gender: str, location: str):
        self.customer_id = customer_id
        self.age         = age
        self.gender      = gender
        self.location    = location
        self.role        = UserRole.CUSTOMER
