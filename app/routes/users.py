from fastapi import APIRouter, Depends, HTTPException, status, Path
from sqlalchemy.orm import Session
from config import get_db
from schemas.users import (
    UserCreateSchema, UserReadSchema, UserUpdateSchema, 
    ResponseUserSchema, ListResponseUserSchema
)
import database.users as user_crud

user_router = APIRouter(
    prefix="/users",
)

# Get a list of users
@user_router.get("/", response_model=ListResponseUserSchema)
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = user_crud.get_users(db, skip=skip, limit=limit)
    return {"code": "success", "status": status.HTTP_200_OK, "response": users}

# Create a new user
@user_router.post("/", response_model=ResponseUserSchema, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    created_user = user_crud.create_user(db, user)
    return {"code": "success", "status": status.HTTP_201_CREATED, "response": created_user}

# Get user details by ID
@user_router.get("/{user_id}", response_model=ResponseUserSchema)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = user_crud.get_user_by_id(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"code": "success", "status": status.HTTP_200_OK, "response": user}

# Update user details
@user_router.put("/{user_id}", response_model=ResponseUserSchema)
def update_user(user_id: int, user: UserUpdateSchema, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    updated_user = user_crud.update_user(db, user_id=user_id, user=user)
    return {"code": "success", "status": status.HTTP_200_OK, "response": updated_user}

# Delete a user
@user_router.delete("/{user_id}", response_model=ResponseUserSchema)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user_crud.delete_user(db, user_id=user_id)
    return {"code": "success", "status": status.HTTP_204_NO_CONTENT, "response": "User deleted"}
