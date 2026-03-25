from enum import Enum 

#this is the model for the status of the payment
#it can be pending, approved, declined or refunded

#Enum is a class that allows us to create a set of named variables 
# So all these variables have a fixed set of values.

class PaymentStatus(Enum):
    PENDING   = "pending"
    APPROVED  = "approved"
    DECLINED  = "declined"
    REFUNDED  = "refunded"
