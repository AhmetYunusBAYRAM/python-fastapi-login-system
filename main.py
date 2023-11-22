from fastapi import FastAPI, Depends, HTTPException, Header
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from datetime import datetime, timedelta
from Model.token_model import Token
from Model.user_model import User
from Model.response_model import Response
from Database.database import fake_users_db

import secrets

app = FastAPI()
access_tokens_db = {}

def authenticate_user(username: str, password: str):
    user = fake_users_db.get(username)
    if user and user["password"] == password:
        return user


def create_access_token(username: str):
    access_token = secrets.token_urlsafe(128)
    expires_in = 900

    access_tokens_db[access_token] = {
        "username": username,
        "expires_at": datetime.utcnow() + timedelta(seconds=expires_in),
        "tenantId": fake_users_db.get(username)["tenantId"]
    }

    return Token(access_token=access_token, expires_in=expires_in, tenantId=fake_users_db.get(username)["tenantId"])


def is_access_token_expired(access_token: str):
    token_info = access_tokens_db.get(access_token)
    if token_info and token_info["expires_at"] > datetime.utcnow():
        return False
    return True


def revoke_access_token(access_token: str):
    if access_token in access_tokens_db:
        del access_tokens_db[access_token]


def clean_expired_access_tokens():
    global access_tokens_db
    access_tokens_db = {token: info for token, info in access_tokens_db.items() if
                        info["expires_at"] > datetime.utcnow()}


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.post("/login", response_model=Response)
async def login_for_access_token(form_data: User):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Kullanıcı adı veya şifre hatalı!")

    clean_expired_access_tokens()
    access_token = create_access_token(form_data.username)
    response = Response(code=200, data=access_token.dict(),
                        message="Başarıyla Login Oldunuz! Access Token süresi 15 dakikadır.")

    return response


@app.get("/all")
def get_all_token():
    response = Response(code=200, data=access_tokens_db, message="Aktif bulunan tüm tokenlar listelenmiştir.")
    return response


@app.get("/token-control")
def get_private_data(token: str = Header(..., token="token")):
    if is_access_token_expired(token):
        revoke_access_token(token)
        raise HTTPException(status_code=400, detail="Access Token süresi geçmiş! Lütfen tekrar login olunuz.")

    userData = access_tokens_db.get(token)
    response = Response(code=200, data={"username": userData["username"], "tenantId": userData["tenantId"]},
                        message="Access Token geçerlidir. 15 dakika sonra yenilemeniz gerekmektedir.")

    return response