from fastapi import APIRouter, Depends, HTTPException, status

from app import schemas, models
from app.authenticator import user_dep

router = APIRouter()


@router.get("/user", response_model=schemas.User)
async def get_user(user: schemas.User = Depends(user_dep)):
    """
    Get the currently logged in user
    """
    return user

