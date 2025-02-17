import uvicorn
import httpx
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from auth.auth_handler import sign_jwt

from schemas.users import UserCreateSchema, UserLoginSchema


from models.users import User
from models.buyer_journey import BuyerJourney, BuyerJourneyQuestions, BuyerJourneyResponses, BuyerJourneySubmission



from routes.users import user_router
from routes.buyer_journey import buyer_journey_router


from config import get_db,engine 

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, JSON
import database.users as user_crud
from sqlalchemy.orm import Session



metadata = MetaData(schema='public')
User.metadata.create_all(bind=engine)
BuyerJourney.metadata.create_all(bind=engine)
BuyerJourneyQuestions.metadata.create_all(bind=engine)
BuyerJourneyResponses.metadata.create_all(bind=engine)
BuyerJourneySubmission.metadata.create_all(bind=engine)


def init_app():
    app = FastAPI(
        title="SmoothAI",
        description="API for user management and authentication",
        version="1.0.0",
        docs_url="/docs",
        redoc_url='/redoc',
        openapi_url="/api/openapi.json",
    )

    # Allowing CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE"],
        allow_headers=["*"]
    )

    # Including User Router
    app.include_router(user_router, prefix='/api', tags=['users'])
    app.include_router(buyer_journey_router, prefix='/api', tags=['buyer_journey'])

    # Root Endpoint
    @app.get("/")
    async def read_root():
        return {"message": "Welcome to SmoothAI!"}

    # Signup API
    @app.post("/signup")
    async def signup(user: UserCreateSchema, db: Session = Depends(get_db)):
        db_user = user_crud.get_user_by_email(db, email=user.email)
        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        created_user = user_crud.create_user(db, user)
        return {
            "token": sign_jwt(user.email),
            "email": created_user.email,
            "name": created_user.name,
            "role": created_user.role
        }

    # Login API
    @app.post("/login")
    async def login(user: UserLoginSchema, db: Session = Depends(get_db)):
        db_user = user_crud.get_user_by_email(db, email=user.email)
        if db_user is None or not user_crud.verify_password(user.password, db_user.password):
            raise HTTPException(status_code=400, detail="Incorrect email or password")
        
        return {
            "token": sign_jwt(user.email),
            "email": db_user.email,
            "name": db_user.name,
            "role": db_user.role
        }

    return app

app = init_app()




# In main.py, add these imports:
from routes.accounts import account_router

# In the init_app function, add this line after including other routers:
app.include_router(account_router, prefix='/api', tags=['accounts'])



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
