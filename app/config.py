from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker
import asyncpg

# Updated local database connection settings
POSTGRES_CONNECTION = {
    "dbname": "appdb",
    "user": "postgres",
    "password": "mayank1309",  
    "host": "localhost",  
    "port": "5432"
}

# Updated DATABASE_URL for local connection
DATABASE_URL = 'postgresql+pg8000://postgres:mayank1309@localhost:5432/appdb'
DATABASE = 'postgresql://postgres:mayank1309@localhost:5432/appdb'

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Async function to connect to PostgreSQL using asyncpg
async def connect_to_db():
    return await asyncpg.connect(DATABASE)

# Async function to close the database connection
async def close_db_connection(connection):
    await connection.close()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
