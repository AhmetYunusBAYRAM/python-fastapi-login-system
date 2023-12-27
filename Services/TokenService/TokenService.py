from Models.TokenModel import TokenModel
from datetime import datetime, timedelta
import secrets

class TokenService:

    @staticmethod
    def new_token(user_id: str):
        access_token = secrets.token_urlsafe(128)
        expires_in = 900
        newTokenModel = TokenModel(user_id = user_id, access_token = access_token, expires_in = datetime.now() + timedelta(seconds=expires_in))
        return newTokenModel

    @staticmethod
    def revoke_access_token(access_token: str):
        if access_token in TokenService.access_tokens_db:
            del TokenService.access_tokens_db[access_token]

    @staticmethod
    def is_access_token_expired(access_token: str):
        token_info = TokenService.access_tokens_db.get(access_token)
        if token_info and token_info["expires_at"] > datetime.utcnow():
            return False
        return True
    @staticmethod
    def authenticate_user(username: str, password: str):
        user = fake_users_db.get(username)
        if user and user["password"] == password:
            return user

    @staticmethod
    def create_access_token(username: str):
        access_token = secrets.token_urlsafe(128)
        expires_in = 900
        TokenService.access_tokens_db[access_token] = {
            "username": username,
            "expires_at": datetime.utcnow() + timedelta(seconds=expires_in),
            "tenantId": fake_users_db.get(username)["tenantId"]
        }

        return TokenModel(
            access_token=access_token,
            expires_in=expires_in,
            tenantId=fake_users_db.get(username)["tenantId"]
        )

    @staticmethod
    def clean_expired_access_tokens():
        global access_tokens_db
        TokenService.access_tokens_db = {token: info for token, info in TokenService.access_tokens_db.items() if
                                         info["expires_at"] > datetime.utcnow()}

