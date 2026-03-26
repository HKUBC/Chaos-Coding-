from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.driver_service import DriverService
from app.services.delivery_service import DeliveryService

router = APIRouter(prefix="/drivers", tags=["Drivers"])
driver_service = DriverService()
delivery_service = DeliveryService()

class DriverRequest(BaseModel):
    driver_id: str
    name: str

# API route to create a new driver. Expects a JSON body with driver_id and name. Returns the created driver details or an error if the driver_id already exists.
@router.post("/")
def create_driver(request: DriverRequest):
    try:
        driver = driver_service.create_driver(request.driver_id, request.name)
        return {"driver_id": driver.driver_id, "name": driver.name, "role": driver.role.value}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# API route to get a driver by their ID. Returns the driver details or a 404 error if the driver is not found.
@router.get("/{driver_id}")
def get_driver(driver_id: str):
    driver = driver_service.get_driver(driver_id)
    if driver is None:
        raise HTTPException(status_code=404, detail="Driver not found")
    return {"driver_id": driver.driver_id, "name": driver.name, "role": driver.role.value}


# API route to get a list of all drivers. Returns a list of driver details.
@router.get("/")
def get_all_drivers():
    drivers = driver_service.get_all_drivers()
    return [{"driver_id": d.driver_id, "name": d.name, "role": d.role.value} for d in drivers]


# API route to assign a driver to a delivery for a given order ID. Expects the driver_id and order_id as path parameters. Returns a success message or an error if the delivery or driver is not found, or if the assignment is invalid.
@router.post("/{driver_id}/assign/{order_id}")
def assign_driver_to_delivery(driver_id: str, order_id: str):
    driver = driver_service.get_driver(driver_id)
    if driver is None:
        raise HTTPException(status_code=404, detail="Driver not found")

    delivery = delivery_service.get_delivery(order_id)
    if delivery is None:
        raise HTTPException(status_code=404, detail="Delivery not found")

    try:
        delivery.assign_driver(driver)
        return {"message": f"Driver {driver_id} assigned to order {order_id}"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
