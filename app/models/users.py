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
    role = Column(String(50), nullable=False)  # 'admin', 'user'
    package = Column(String(50), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Add relationship for accounts created by this admin
    created_accounts = relationship("Account", back_populates="admin")
    
    @property
    def is_admin(self):
        return self.role == "admin"