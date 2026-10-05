from jose import jwt, JWTError
from datetime import datetime, timedelta
from . import schemas
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme= OAuth2PasswordBearer("login")

#SECRET_KEY
SECRET_KEY= "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"

#Algorithm
ALGORITHM = "HS256"

#Experation_time
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode= data.copy()
    expire= datetime.utcnow() + timedelta(minutes= ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt= jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token: str, details_exception):

    try:
        payload= jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id= payload.get("user_id")

        if user_id  is None:
            raise details_exception
        token_data= schemas.TokenData(user_id = user_id )
    except JWTError:
        raise details_exception
    return token_data


def get_current_user(token: str= Depends(oauth2_scheme)):

    details_exception= HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, detail="Could not validate details", headers={"WWW-Authenticte": "Bearer"})

    return verify_access_token(token, details_exception)
    