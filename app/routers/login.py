from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app import database_models
from app.database import get_db
from app import utils
from app import oauth2

router = APIRouter()

#oautj2
@router.post("/")
async def login(db: Annotated[Session, Depends(get_db)], user_credencials: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = db.query(database_models.Users).filter(database_models.Users.username == user_credencials.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")
    
    if not utils.verify(user_credencials.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")
    
    access_token = oauth2.create_access_token({"username": user.username})
    
    return {"access_token" : access_token, "token_type": "bearer"}

