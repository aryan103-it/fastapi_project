from fastapi import  Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func, case
from typing import List, Optional
from .. import models, schemas, oauth2
from ..database import  get_db

router= APIRouter(
    prefix= "/posts",
    tags=["Posts"]
)

@router.get("/", response_model=list[schemas.PostVote])
def get_post(db: Session= Depends(get_db), limit: int= 10, skip : int= 0, search: Optional[str]= ""):
    # cursor.execute("""SELECT * FROM post """)
    # posts= cursor.fetchall() 

    # posts= db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    posts= db.query(models.Post, func.count(case((models.Votes.dir==1, 1))).label("up_votes"),func.count(case((models.Votes.dir == -1, 1))).label("down_votes")).join(models.Votes, models.Post.id == models.Votes.post_id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    return [
        {
            "post": post,
            "up_votes": up_votes,
            "down_votes": down_votes
        }
        for post, up_votes, down_votes in posts
    ]

@router.post("/",response_model=schemas.PostResponse)
def posts(post: schemas.PostCreate, db:Session = Depends(get_db), user: int= Depends(oauth2.get_current_user)):
    new_post= models.Post(**post.dict(), user_id=user)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post 


@router.get("/{id}", response_model=schemas.PostVote)
def get_post(id: int, db:Session=Depends(get_db)):
    # post=db.query(models.Post).filter(models.Post.id == id).first()
    post=db.query(models.Post, func.count(case((models.Votes.dir==1, 1))).label("up_votes"),func.count(case((models.Votes.dir == -1, 1))).label("down_votes")).join(models.Votes, models.Post.id == models.Votes.post_id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post with id: {id}, Not Found")
    post, up_votes, down_votes = post
    return {
        "post": post,
        "up_votes": up_votes,
        "down_votes": down_votes
    }


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session=Depends(get_db),user: int= Depends(oauth2.get_current_user)):

    posts = db.query(models.Post).filter(models.Post.id == id).first()

    if  posts == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f"Post with id:{id}, NOT_FOUND")
    if user != posts.user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not Authorized")
    
    db.delete(posts)
    db.commit()
    return Response(status_code= status.HTTP_204_NO_CONTENT)


@router.put("/{id}",response_model=schemas.PostResponse)
def update_post(id: int, post: schemas.PostUpdate,db: Session=Depends(get_db),user: int= Depends(oauth2.get_current_user)):

    post_query= db.query(models.Post).filter(models.Post.id==id)
    posts=post_query.first()

    if posts == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f"Post with id:{id}, NOT_FOUND")
    if user != posts.user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not Authorized")    
    post_query.update(post.dict(), synchronize_session=False)
    db.commit()
    db.refresh(posts)
    return posts