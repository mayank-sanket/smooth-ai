from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from config import get_db
from schemas.accounts import AccountCreateSchema, AccountReadSchema, AccountUpdateSchema, AccountListResponse
from models.accounts import Account
from models.users import User
from auth.auth_bearer import JWTBearer
from auth.auth_handler import decode_jwt
import database.users as user_crud
from database.password import get_password_hash

account_router = APIRouter()

def get_current_admin(db: Session, token: str = Depends(JWTBearer())):
    email = decode_jwt(token)["user_id"]
    user = user_crud.get_user_by_email(db, email)
    if not user or user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Only admin users can perform this action"
        )
    return user

@account_router.post("/accounts", response_model=AccountReadSchema)
async def create_account(
    account: AccountCreateSchema,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    # Check if email already exists
    if user_crud.get_user_by_email(db, account.email):
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )
    
    # Create new account
    db_account = Account(
        name=account.name,
        email=account.email,
        password=get_password_hash(account.password),
        role=account.role,
        package=account.package,
        created_by=current_admin.user_id
    )
    
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account

@account_router.get("/accounts", response_model=AccountListResponse)
async def list_accounts(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    accounts = db.query(Account).offset(skip).limit(limit).all()
    return AccountListResponse(
        code="success",
        status=200,
        response=accounts
    )

@account_router.get("/accounts/{user_id}", response_model=AccountReadSchema)
async def get_account(
    user_id: int,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    account = db.query(Account).filter(Account.user_id == user_id).first()
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account

@account_router.put("/accounts/{user_id}", response_model=AccountReadSchema)
async def update_account(
    user_id: int,
    account_update: AccountUpdateSchema,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    db_account = db.query(Account).filter(Account.user_id == user_id).first()
    if not db_account:
        raise HTTPException(status_code=404, detail="Account not found")
    
    update_data = account_update.dict(exclude_unset=True)
    if "password" in update_data:
        update_data["password"] = get_password_hash(update_data["password"])
    
    for field, value in update_data.items():
        setattr(db_account, field, value)
    
    db.commit()
    db.refresh(db_account)
    return db_account

@account_router.delete("/accounts/{user_id}")
async def delete_account(
    user_id: int,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    account = db.query(Account).filter(Account.user_id == user_id).first()
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    
    db.delete(account)
    db.commit()
    return {"message": "Account deleted successfully"}