from typing import List, Optional, Union
from pydantic import BaseModel, Field
from datetime import datetime

# Schema for user login
class UserLoginSchema(BaseModel):
    email: str
    password: str

# Base schema for user (shared fields)
class UserBaseSchema(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    role: Optional[str] = None  # 'admin', 'customer', etc.
    package: Optional[str] = None  # Subscription package

# Schema for creating a user
class UserCreateSchema(UserBaseSchema):
    name: str
    email: str
    password: str
    role: str

# Schema for reading user details
class UserReadSchema(UserBaseSchema):
    user_id: int
    created_at: datetime

# Schema for updating a user
class UserUpdateSchema(UserBaseSchema):
    password: Optional[str] = None  # Optional for update

# Schema for a single user response
class ResponseUserSchema(BaseModel):
    response: Union[str, UserReadSchema] = Field(...)

# Schema for a list of users
class ListResponseUserSchema(BaseModel):
    code: str
    status: int
    response: List[UserReadSchema] = Field(...)
