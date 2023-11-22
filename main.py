from fastapi import FastAPI
from Controllers.UserController.UserController import router as user_router
from Controllers.SecurityController.SecurityController import router as security_router

app = FastAPI()

app.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(security_router, prefix="/security", tags=["security"])