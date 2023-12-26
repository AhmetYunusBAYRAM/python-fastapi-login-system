from pydantic import BaseModel
from typing import Optional

class LoginModel(BaseModel):
    user_login_type : int
    user_auth_token : Optional[str] = None
    user_email: str
    user_password: str
