from fastapi import APIRouter
from Models.ResponseModel import ResponseModel
from Models.UserModel import UserModel
from Models.LoginModel import LoginModel
from Services.LoginService.LoginService import LoginService
from Services.UserService.UserService import UserService

loginService = LoginService()
router = APIRouter()

@router.post("/create-account", response_model=ResponseModel)
async def create_user(form_data: UserModel):
    return await UserService.signup(userModel=form_data)


@router.get("/login", response_model=ResponseModel)
async def login(form_data: LoginModel):
    return await UserService.login(form_data)