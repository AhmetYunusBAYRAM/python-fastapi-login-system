from fastapi import APIRouter,HTTPException
from Models.ResponseModel import ResponseModel
from Models.UserModel import UserModel
from Models.LoginModel import LoginModel
from Services.LoginService.LoginService import LoginService
from Services.UserService.UserService import UserService

loginService = LoginService()
router = APIRouter()

@router.post("/create-account", response_model=ResponseModel)
async def create_user(form_data: UserModel):
    response = await UserService.signup(userModel=form_data)
    if response.code != 200:
        raise HTTPException(status_code=400, detail="Bu mail adresine ait hesap bulunmaktadır.")
    return response


@router.get("/login", response_model=ResponseModel)
async def login(form_data: LoginModel):
    response = await UserService.login(loginModel=form_data)
    if response.code != 200:
        raise HTTPException(status_code=400, detail="Kullanıcı adı veya parola yanlış!")
    return response