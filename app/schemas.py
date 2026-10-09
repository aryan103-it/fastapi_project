from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Annotated


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
    user: UserResponse

    class Config:
        from_attributes = True

class PostVote(BaseModel):
    post: PostResponse
    up_votes:int
    down_votes:int

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    user_id : int

class Vote(BaseModel):
    post_id: int
    dir: Annotated[int, Field(ge=-1, le=1)]