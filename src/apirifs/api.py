""" FastAPI"""

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

from apirifs.models.model_example import User, Book, Borrow

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="dev")


@app.get("/health")
async def healthcheck():
    """Healthcheck endpoint"""
    return 200


@app.post("/user", status_code=202)
async def create_user(user: User, token: str = Depends(oauth2_scheme)):
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


@app.get("/user/{user_id}", status_code=200)
async def get_user(user_id, token: str = Depends(oauth2_scheme)):
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


@app.patch("/user/{user_id}", status_code=202)
async def patch_user(user_id, user: User, token: str = Depends(oauth2_scheme)):
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


@app.post("/book", status_code=202)
async def create_book(book: Book, token: str = Depends(oauth2_scheme)):
    """Create book endpoint

    Parameters
    ----------
    book : Book
        Book object

    Returns
    -------
    response: str
        Response in json format
    status_code: int
        Status code
    """
    return {"message": "Book created", "book": book}


@app.get("/book/{book_id}", status_code=200)
async def get_book(book_id, token: str = Depends(oauth2_scheme)):
    """Get book endpoint

    Parameters
    ----------
    book_id : str
        Book id

    Returns
    -------
    response: str
        Response in json format
    status_code: int
        Status code
    """
    return 200


@app.patch("/book/{book_id}", status_code=200)
async def patch_book(book_id, book: Book, token: str = Depends(oauth2_scheme)):
    """Update user endpoint

    Parameters
    ----------
    book_id : str
        Book id
    book : Book
        Book object

    Returns
    -------
    response: str
        Response in json format
    status_code: int
        Status code
    """
    return {"message": "Book updated", "book": book}


@app.post("/borrow", status_code=202)
async def create_borrow(borrow: Borrow, token: str = Depends(oauth2_scheme)):
    """Create borrow endpoint

    Parameters
    ----------
    borrow : Borrow
        Borrow object

    Returns
    -------
    response: str
        Response in json format
    status_code: int
        Status code
    """
    return {"message": "Borrow created", "borrow": borrow}


@app.get("/borrow/{borrow_id}", status_code=200)
async def get_borrow(borrow_id, token: str = Depends(oauth2_scheme)):
    """Get book endpoint

    Parameters
    ----------
    borrow_id : str
        Borrow id

    Returns
    -------
    response: str
        Response in json format
    status_code: int
        Status code
    """
    return 200


@app.patch("/borrow/{borrow_id}", status_code=200)
async def patch_borrow(borrow_id, borrow: Borrow, token: str = Depends(oauth2_scheme)):
    """Update user endpoint

    Parameters
    ----------
    borrow_id : str
        Borrow id
    borrow : Borrow
        Borrow object

    Returns
    -------
    response: str
        Response in json format
    status_code: int
        Status code
    """
    return {"message": "Borrow updated", "borrow": borrow}
