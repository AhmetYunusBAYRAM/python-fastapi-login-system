from pydantic import BaseModel
from datetime import datetime, timedelta

class TokenModel(BaseModel):
    access_token: str
    user_id: str
    expires_in: datetime
