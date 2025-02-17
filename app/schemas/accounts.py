from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime
from schemas.users import UserReadSchema

class AccountCreateSchema(BaseModel):
    name: str
    email: str
    password: str
    role: str = "user"  # Default role is user
    package: Optional[str] = None

class AccountReadSchema(BaseModel):
    user_id: int
    name: str
    email: str
    role: str
    package: Optional[str]
    created_at: datetime
    created_by: int  # Admin user ID who created this account

class AccountUpdateSchema(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    package: Optional[str] = None
    role: Optional[str] = None

class AccountListResponse(BaseModel):
    code: str
    status: int
    response: List[AccountReadSchema] = Field(...)