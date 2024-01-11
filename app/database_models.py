from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Identity, Column, Integer, String, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy import func

class Base(DeclarativeBase):
    pass

class Todos(Base):
    __tablename__ = "totdos"
    id = Column(Integer, Identity(start= 1, increment= 1), primary_key=True)
    title = Column(String(50), unique=True, nullable=False)
    description = Column(String(50), nullable=False)
    owner_username = Column(String(50), ForeignKey("users.username", ondelete="CASCADE"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), default=func.current_timestamp())
    
class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, Identity(start= 1, increment= 1), primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    hashed_password = Column(String(100), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), default=func.current_timestamp())