from Database.TokenDataBase import TokenDataBase
import asyncio
class BackGroundService:
    async def background_task():
        while True:
            await asyncio.sleep(60)
            TokenDataBase.delete_token()