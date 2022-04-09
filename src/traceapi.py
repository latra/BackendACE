import imp
from typing import Optional
from src.auth import token as oauth_tokens
from src.auth import login as oauth_login
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from src.controller.user import User


app = FastAPI()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")



async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = oauth_tokens.is_valid(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_active_user(current_user: str = Depends(get_current_user)):
    return current_user


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    login = oauth_login.login(form_data.username, form_data.password)  
    if not login:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"access_token": oauth_tokens.create_token(form_data.username), "token_type": "bearer"}



@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return "ok"