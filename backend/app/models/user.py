from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.db.config import Base

class User(Base):
    __tablename__ = "users"
    
    pass
