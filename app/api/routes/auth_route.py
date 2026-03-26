from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.auth_service import AuthService
from app.model.user_role import UserRole

router = APIRouter(prefix="/auth", tags=["auth"])
service = AuthService()

class SignUpRequest(BaseModel):
    user_id: str
    password: str
    role: UserRole

class LoginRequest(BaseModel):
    user_id: str
    password: str

class TokenRequest(BaseModel):
    token: str

@router.post("/signup")
def sign_up(request: SignUpRequest):
    try:
        service.sign_up(request.user_id, request.password, request.role)
        return {"message": f"User {request.user_id} created successfully."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login(request: LoginRequest):
    try:
        token = service.login(request.user_id, request.password)
        return {"token": token}
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
