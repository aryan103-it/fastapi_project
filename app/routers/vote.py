from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils, oauth2
from ..database import get_db

router = APIRouter(prefix="/votes", tags=["Vote"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(
    vote: schemas.Vote,
    db: Session = Depends(get_db),
    user: int = Depends(oauth2.get_current_user),
):
    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {vote.post_id} NOT FOUND",
        )

    find_vote = (
        db.query(models.Votes)
        .filter(models.Votes.post_id == vote.post_id, models.Votes.user_id == user)
        .first()
    )
    if vote.dir == 1:
        find_upvote = (
            db.query(models.Votes)
            .filter(
                models.Votes.post_id == vote.post_id,
                models.Votes.user_id == user,
                dir == 1,
            )
            .first()
        )
        if find_upvote:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"User with id {user} already voted",
            )

        new_vote = models.Votes(post_id=vote.post_id, user_id=user, dir=1)
        db.add(new_vote)
        db.commit()
        return "Upvoted Sucessfully!!!"
    if vote.dir == -1:
        find_downvote = (
            db.query(models.Votes)
            .filter(
                models.Votes.post_id == vote.post_id,
                models.Votes.user_id == user,
                dir == -1,
            )
            .first()
        )
        if find_downvote:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"User with id {user} already voted",
            )

        new_vote = models.Votes(post_id=vote.post_id, user_id=user, dir=-1)
        db.add(new_vote)
        db.commit()
        return "Downvoted Sucessfully!!!"

    if vote.dir == 0:
        if not find_vote:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"User {user} don't have vote in post {vote.post_id}",
            )
        db.delete(find_vote)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
