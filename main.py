from fastapi import FastAPI
from Services.BackGroundService.BackGroundService import BackGroundService
from Controllers.UserController.UserController import router as user_router
import asyncio

app = FastAPI()

app.include_router(user_router, prefix="/user", tags=["user"])
@app.on_event("startup")
async def startup_event():
    await asyncio.create_task(BackGroundService.background_task())
