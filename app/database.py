from app.app_settings import get_settings
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from app import database_models
import urllib.parse


settings = get_settings()

username = settings.ORACLE_DB_USERNAME
password = urllib.parse.quote_plus(settings.ORACLE_DB_PASSWORD)
dsn = settings.ORACLE_DB_DSN

#engine = create_engine(f"oracle+oracledb://:@", connect_args={"user": username,"password" : password,"dsn" :dsn})
engine = create_engine(f"oracle+oracledb://{username}:{password}@{dsn}")

database_models.Base.metadata.create_all(bind=engine)

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()
