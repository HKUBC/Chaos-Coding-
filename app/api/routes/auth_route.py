from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.services.auth_service import AuthService
from app.model.user_role import UserRole


router = APIRouter(prefix="/auth", tags=["Auth"])
service = AuthService()

class SignUpRequest(BaseModel):
    user_id: str
    password: str
    role: UserRole = UserRole.CUSTOMER
    restaurant_id: Optional[int] = None
    full_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    # Restaurant owner extras
    restaurant_name: Optional[str] = None
    # Driver extras
    vehicle: Optional[str] = None
    license_plate: Optional[str] = None

class LoginRequest(BaseModel):
    user_id: str
    password: str

class TokenRequest(BaseModel):
    token: str

@router.post("/signup")
def sign_up(request: SignUpRequest):
    try:
        profile = {k: v for k, v in {
            "full_name":       request.full_name,
            "email":           request.email,
            "phone":           request.phone,
            "restaurant_name": request.restaurant_name,
            "vehicle":         request.vehicle,
            "license_plate":   request.license_plate,
        }.items() if v is not None}
        service.sign_up(request.user_id, request.password, request.role,
                        request.restaurant_id, profile or None)
        return {"message": f"User {request.user_id} created successfully."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login(request: LoginRequest):
    try:
        token = service.login(request.user_id, request.password)
        result = service.get_me(token)
        result["token"] = token
        return result
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))

@router.post("/me")
def get_me(request: TokenRequest):
    try:
        return service.get_me(request.token)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))

@router.post("/logout")
def logout(request: TokenRequest):
    try:
        service.logout(request.token)
        return {"message": "Logged out successfully."}
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))

@router.post("/validate")
def validate_token(request: TokenRequest):
    try:
        user_id = service.validate_token(request.token)
        return {"user_id": user_id}
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
