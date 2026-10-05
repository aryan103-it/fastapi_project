from fastapi import  Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, oauth2
from ..database import  get_db

router= APIRouter(
    prefix= "/posts",
    tags=["Posts"]
)

@router.get("/", response_model=list[schemas.PostResponse])
def get_post(db: Session= Depends(get_db)):
    # cursor.execute("""SELECT * FROM post """)
    # posts= cursor.fetchall() 

    posts= db.query(models.Post).all()
    print(posts)
    return posts


@router.post("/",response_model=schemas.PostResponse)
def posts(post: schemas.PostCreate, db:Session = Depends(get_db), user: int= Depends(oauth2.get_current_user)):
    print(user)
    new_post= models.Post(**post.dict(), user_id=user)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post 


@router.get("/{id}", response_model=schemas.PostResponse)
def get_post(id: int, db:Session=Depends(get_db)):
    post=db.query(models.Post).filter(models.Post.id == id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post with id: {id}, Not Found")
    return post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session=Depends(get_db),user_id: int= Depends(oauth2.get_current_user)):

    posts = db.query(models.Post).filter(models.Post.id == id)
    if  posts.first()== None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f"Post with id:{id}, NOT_FOUND")
    
    posts.delete(synchronize_session=False)
    db.commit()
    return Response(status_code= status.HTTP_204_NO_CONTENT)


@router.put("/{id}",response_model=schemas.PostResponse)
def update_post(id: int, post: schemas.PostUpdate,db: Session=Depends(get_db),user_id: int= Depends(oauth2.get_current_user)):

    post_query= db.query(models.Post).filter(models.Post.id==id)
    updated_post= post_query.first()

    if updated_post == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f"Post with id:{id}, NOT_FOUND")
    
    post_query.update(post.dict(), synchronize_session=False)
    db.commit()

    return post_query.first() 