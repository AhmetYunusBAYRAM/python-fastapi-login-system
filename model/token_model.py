from pydantic import BaseModel
from typing import Optional

class Token(BaseModel):
    access_token: str
    tenantId: str
    expires_in: int
