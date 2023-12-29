from Database.UserDataBase import UserDatabase
from Database.TokenDataBase import TokenDataBase
from Services.TokenService import TokenService
from Models.UserModel import UserModel
from Models.ResponseModel import ResponseModel
from Models.LoginModel import LoginModel
import asyncio


class UserService:

    async def signup(userModel: UserModel):
        if userModel.user_login_type == 1:
            return UserDatabase.create_user_account(userModel)

    async def login(loginModel: LoginModel):

        if loginModel.user_login_type == 1:
            user_id = UserDatabase.login_user_email_and_password(loginModel)
            if user_id:
                tokenService = TokenService
                tokenModel = tokenService.TokenService.new_token(user_id[0])
                TokenDataBase.create_token(tokenModel)
                return ResponseModel(data= tokenModel.dict(), message="Başarıyla oturum açıldı!", code=200)
            else :
                return  ResponseModel(data= loginModel.user_email,message="Kullanıcı adı veya parola yanlış!",code = 400)
