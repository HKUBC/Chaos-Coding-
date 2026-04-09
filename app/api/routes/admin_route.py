from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.api.routes.auth_route import service as auth_service
from app.services.restaurant_service import RestaurantService
from app.services.delivery_service import DeliveryService
from app.model.user_role import UserRole

router = APIRouter(prefix="/admin", tags=["Admin"])
restaurant_service = RestaurantService()
delivery_service = DeliveryService()


def _require_admin(token: str):
    try:
        auth_service.require_admin(token)
    except ValueError as e:
        raise HTTPException(status_code=403, detail=str(e))


# ── System stats ────────────────────────────────────────────────────────────

@router.get("/stats")
def get_stats(token: str):
    _require_admin(token)
    users = auth_service.get_all_users()
    restaurants = restaurant_service.get_all_restaurants_info()
    deliveries = delivery_service.get_all_deliveries()

    role_counts = {}
    for u in users:
        role_counts[u["role"]] = role_counts.get(u["role"], 0) + 1

    return {
        "total_users":       len(users),
        "total_restaurants": len(restaurants),
        "total_deliveries":  len(deliveries),
        "open_restaurants":  sum(1 for r in restaurants if r["is_open"]),
        "users_by_role":     role_counts,
    }


# ── User management ─────────────────────────────────────────────────────────

@router.get("/users")
def get_all_users(token: str):
    _require_admin(token)
    return auth_service.get_all_users()


class UpdateRoleRequest(BaseModel):
    token: str
    new_role: str


@router.patch("/users/{user_id}/role")
def update_user_role(user_id: str, request: UpdateRoleRequest):
    _require_admin(request.token)
    try:
        new_role = UserRole(request.new_role)
    except ValueError:
        raise HTTPException(status_code=400, detail=f"Invalid role '{request.new_role}'.")
    try:
        auth_service.update_user_role(user_id, new_role)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return {"message": f"Role for '{user_id}' updated to '{request.new_role}'."}


class TokenBody(BaseModel):
    token: str


@router.delete("/users/{user_id}")
def delete_user(user_id: str, request: TokenBody):
    _require_admin(request.token)
    try:
        auth_service.delete_user(user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return {"message": f"User '{user_id}' deleted."}


# ── Restaurant management ───────────────────────────────────────────────────

@router.get("/restaurants")
def get_all_restaurants(token: str):
    _require_admin(token)
    return restaurant_service.get_all_restaurants_info()


@router.post("/restaurants/{restaurant_id}/toggle")
def toggle_restaurant(restaurant_id: int, request: TokenBody):
    _require_admin(request.token)
    try:
        new_state = restaurant_service.toggle_restaurant_open(restaurant_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    state_str = "open" if new_state else "closed"
    return {"message": f"Restaurant {restaurant_id} is now {state_str}.", "is_open": new_state}


# ── Delivery management ─────────────────────────────────────────────────────

@router.get("/deliveries")
def get_all_deliveries(token: str):
    _require_admin(token)
    deliveries = delivery_service.get_all_deliveries()
    return [
        {
            "order_id":  d.delivery_id,
            "status":    d.status.value,
            "driver":    d.driver.driver_id if d.driver else None,
            "distance":  d.delivery_distance,
            "time":      d.delivery_time,
        }
        for d in deliveries
    ]
