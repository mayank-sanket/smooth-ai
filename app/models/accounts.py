from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config import Base
from database.mixins import TimestampMixin
from datetime import datetime

class Account(Base, TimestampMixin):
    __tablename__ = "accounts"
    
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False, default="user")
    package = Column(String(50), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    created_by = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    
    # Relationship with the admin who created this account
    admin = relationship("User", back_populates="created_accounts")