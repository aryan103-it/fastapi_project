from pydantic import BaseModel, EmailStr
from datetime import datetime

class PostBase(BaseModel):
    title: str
    content: str
    published: bool= True


class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    pass 

class PostResponse(PostBase):

    id: int
    created_at: datetime
    user_id: int

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    email:EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes= True

class UserLogin(BaseModel):
    email:EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    user_id : int