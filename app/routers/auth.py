from fastapi import  Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from .. import models, schemas, utils, oauth2
from .. database import get_db

router= APIRouter(
    tags= ["Authentication"]
)

@router.post("/login", response_model= schemas.Token)
# def login(user_details: schemas.UserLogin, db:Session=Depends(get_db)):
def login(user_details: OAuth2PasswordRequestForm=Depends(), db:Session=Depends(get_db)):
    # user= db.query(models.Users).filter(models.Users.email== user_details.email).first()
    user= db.query(models.Users).filter(models.Users.email== user_details.username).first()


    if not user:
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail= "Invalid email or password")

    if not utils.verify(user_details.password, user.password):
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail= "Invalid email or password")

    #create token
    access_token= oauth2.create_access_token(data= {"user_id" : user.id})

    #return token
    return {"access_token": access_token, "token_type": "bearer"}