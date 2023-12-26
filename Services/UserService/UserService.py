from Database.UserDataBase import UserDatabase
from Models.UserModel import UserModel
from Models.LoginModel import LoginModel
import asyncio
class UserService:
    async def signup(userModel : UserModel) :
       if userModel.user_login_type == 1:
           return UserDatabase.create_user_account(userModel)

    async def login(loginModel : LoginModel) :
        if loginModel.user_login_type == 1:
            return UserDatabase.login_user_email_and_password(loginModel)
