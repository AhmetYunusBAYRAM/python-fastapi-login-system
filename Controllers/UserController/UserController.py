from fastapi import APIRouter
from Models.ResponseModel import ResponseModel
from Models.UserModel import UserModel
from Services.LoginService.LoginService import LoginService

loginService = LoginService()
router = APIRouter()

@router.post("/login", response_model=ResponseModel)
async def login(form_data: UserModel):
    response = await loginService.login_for_access_token(form_data)
    return response