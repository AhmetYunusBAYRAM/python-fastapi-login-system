from fastapi import HTTPException
from Models.ResponseModel import ResponseModel
from Models.UserModel import UserModel
from Services.TokenService.TokenService import TokenService


class LoginService:
    @staticmethod
    async def login_for_access_token(form_data: UserModel):
        user = TokenService.authenticate_user(form_data.username, form_data.password)
        if not user:
            raise HTTPException(status_code=400, detail="Kullanıcı adı veya şifre hatalı!")

        TokenService.clean_expired_access_tokens()
        access_token = TokenService.create_access_token(form_data.username)
        response = ResponseModel(
            code=200,
            data=access_token.dict(),
            message="Başarıyla Login Oldunuz! Access Token süresi 15 dakikadır."
        )

        return response