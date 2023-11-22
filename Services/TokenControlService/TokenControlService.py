from fastapi import APIRouter,HTTPException,Header
from Models.ResponseModel import ResponseModel
from Services.TokenService.TokenService import TokenService
router = APIRouter()

tokenController = TokenService()

class TokenControlService:

    @staticmethod
    def control_access_token(token: str):
        if tokenController.is_access_token_expired(token):
            tokenController.revoke_access_token(token)
            raise HTTPException(status_code=401, detail="Access Token'ın süresi doldu!")

        userData = tokenController.access_tokens_db.get(token)

        response = ResponseModel(code=200, data={"username": userData["username"], "tenantId": userData["tenantId"]},
                        message="Access Token süresi mevcut!")
        return response