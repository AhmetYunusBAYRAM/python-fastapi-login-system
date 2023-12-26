from pydantic import BaseModel

class UserModel(BaseModel):
    user_id : str
    user_detail_id : int
    user_profile_image: str
    user_first_name: str
    user_last_name: str
    user_email: str
    user_login_type: int
    user_country_id: int
    user_password: int
