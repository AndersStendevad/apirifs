""" FastAPI"""

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBearer
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

from apirifs.models.model_example import User, Book, Borrow
from apirifs.settings import Settings

settings = Settings()
security = HTTPBearer()
secret_key = settings.security_admin_password

app = FastAPI()
app.add_middleware(HTTPSRedirectMiddleware)

def api_key_auth(api_key: str = Depends(security)):
    if api_key.credentials != secret_key.get_secret_value():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="UNAUTHORIZED"
        )


@app.get("/health")
async def healthcheck():
    """Healthcheck endpoint"""
    return 200


@app.post("/user", status_code=202, dependencies=[Depends(api_key_auth)])
async def create_user(user: User): 
    """Create user endpoint

    Parameters
    ----------
    user : User
        User object

    Returns
    -------
    response: str
        Response in json format
    status_code: int
        Status code
    """
    return {"message": "User created", "user": user}


@app.get("/user/{user_id}", status_code=200, dependencies=[Depends(api_key_auth)])
async def get_user(user_id):
    """Get user endpoint

    Parameters
    ----------
    user_id : str
        User id

    Returns
    -------
    response: str
        Response in json format
    status_code: int
        Status code
    """
    return 200


@app.patch("/user/{user_id}", status_code=202, dependencies=[Depends(api_key_auth)])
async def patch_user(user_id, user: User):
    """Update user endpoint

    Parameters
    ----------
    user_id : str
        User id
    user : User
        User object

    Returns
    -------
    response: str
        Response in json format
    status_code: int
        Status code
    """
    return {"message": "User updated", "user": user}


