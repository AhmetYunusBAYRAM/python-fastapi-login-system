from pydantic import BaseModel
from typing import Optional

class TokenModel(BaseModel):
    access_token: str
    tenantId: str
    expires_in: int
