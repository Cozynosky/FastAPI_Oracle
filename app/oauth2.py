from datetime import datetime, timedelta
from typing import Annotated
from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from app.app_settings import get_settings
from fastapi.security import OAuth2PasswordBearer

ouath2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

settings = get_settings()

def create_access_token(data: dict):
    
    data_copy = data.copy()
    
    expiration_time = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRATION_MINUTES)
    data_copy.update({"exp": expiration_time})
    
    token = jwt.encode(data_copy, algorithm=settings.ALGORITHM, key=settings.SECRET_KEY)
    
    return token

def get_current_username(token: Annotated[str, Depends(ouath2_scheme)]):
    try: 
        payload = jwt.decode(token, key=settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("username")
        
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Cloud not validate credentials", headers={"WWW-Authenticate":"Bearer"})
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Cloud not validate credentials", headers={"WWW-Authenticate":"Bearer"})
    return username