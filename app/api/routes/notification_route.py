from fastapi import APIRouter, HTTPException
from app.services.notification_service import NotificationService

router = APIRouter(prefix="/notifications", tags=["notifications"])
service = NotificationService()

#This route will return all notifications for a given recipient (restaurant or customer). 
@router.get("/{recipient_id}")
# This route method will get all notifications for a restaurant or customer by their id, if there are no notifications then it will return an empty list
def get_notifications(recipient_id: str):
    """Return all notifications for a restaurant or customer."""
    return service.get_notifications(recipient_id)
