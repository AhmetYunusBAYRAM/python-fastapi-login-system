from fastapi import APIRouter,HTTPException,Header
from Models.ResponseModel import ResponseModel
from Services.TokenControlService.TokenControlService import TokenControlService
router = APIRouter()
tokenServiceControl = TokenControlService()

@router.get("/token-control")
def get_private_data(token: str = Header(..., token="token")):
    response = tokenServiceControl.control_access_token(token)

    return response