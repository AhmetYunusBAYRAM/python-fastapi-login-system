from fastapi import FastAPI
from Database.TokenDataBase import TokenDataBase
from Controllers.UserController.UserController import router as user_router
import asyncio


app = FastAPI()
app.include_router(user_router, prefix="/user", tags=["user"])

async def background_task():
    while True:
        TokenDataBase.delete_token()
        await asyncio.sleep(60)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(background_task())