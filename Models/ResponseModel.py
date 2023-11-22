from pydantic import BaseModel
from typing import Dict, Any

class ResponseModel(BaseModel):
    code: int
    message: str
    data: Dict[str, Any]
