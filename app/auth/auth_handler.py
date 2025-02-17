import time
import jwt
import os
from typing import Dict
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get the JWT secret and algorithm from the environment variables
JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")

# Function to sign JWT tokens
def sign_jwt(email: str) -> Dict[str, str]:
    payload = {
        "email": email,
        "expires": time.time() + 3600  # Token expires in 1 hour
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token

# Function to decode JWT tokens
def decode_jwt(token: str) -> Dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return None
