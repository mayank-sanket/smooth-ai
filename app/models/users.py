# models/user.py
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from config import Base
from database.mixins import TimestampMixin
from datetime import datetime


class User(Base, TimestampMixin):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(255), nullable=False)  
    role = Column(String(50), nullable=False)  # E.g. 'admin', 'customer'
    package = Column(String(50), nullable=True)  # Subscription package
    created_at = Column(DateTime, default=datetime.utcnow)

