from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time

from sqlalchemy.orm import Session
from . import models, schemas, utils
from .database import  get_db, engine
from .routers import post, user, auth


models.Base.metadata.create_all(bind=engine)

app = FastAPI()




my_posts=[{"title": "title 1", "content": 'content 1', "id": 1}, 
          {"title": "title 2", "content": 'content 2', "id": 2}
         ]


while True:
    try:
        conn= psycopg2.connect(host='localhost' , database='fastapi' , user='postgres', password='Cket@128', cursor_factory=RealDictCursor)
        cursor=conn.cursor()
        print('Database Conected Successfully')
        break

    except Exception as e:
        print('Database Connection Failed')
        print("ERROR: ", e)
        time.sleep(2)


def find_id(id):
    for post in my_posts:
        if post["id"] == id:
            return post

def find_post_index(id):
    for i, post in enumerate(my_posts):
        if post["id"] == id:
            return i

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

