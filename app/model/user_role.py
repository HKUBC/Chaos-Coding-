from enum import Enum

# This is the model for the roles in the system

class UserRole(Enum):
    CUSTOMER         = "customer"
    RESTAURANT_OWNER = "restaurant_owner"
    DRIVER           = "driver"
