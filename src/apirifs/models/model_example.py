""" Example for how to write models to use in API """
from enum import Enum
from uuid import uuid4
from pydantic import BaseModel, Field, ValidationError, validator, Extra


class Gender(str, Enum):
    """Enum for Gender"""

    male = "male"
    female = "female"
    other = "other"
    not_given = "not_given"


class User(BaseModel):
    """User Model"""

    id_: str = Field(default_factory=lambda: "user-" + uuid4().hex, alias="xt/id")
    name: str = Field(..., alias="user/name")
    gender: Gender = Field(..., alias="user/gender")

    @validator("name")
    def name_must_contain_space(cls, v):
        """Makes sure that name has a space in it"""
        if " " not in v:
            raise ValidationError("must contain a space")
        return v.title()

    class Config:
        """Example for FastAPI"""

        extra = Extra.forbid
        schema_extra = {"example": {"user/name": "Alice Bob", "user/gender": "female"}}


class Book(BaseModel):
    """Book Model"""

    id_: str = Field(default_factory=lambda: "book-" + uuid4().hex, alias="xt/id")
    author: str = Field(..., alias="book/author")
    title: str = Field(..., alias="book/title")
    edition: str = Field(..., alias="book/edition")

    class Config:
        """Example for FastAPI"""

        extra = Extra.forbid
        schema_extra = {
            "example": {
                "book/author": "John Doe",
                "book/title": "English Dictionary",
                "book/edition": "1st Edition",
            }
        }


class Borrow(BaseModel):
    """Borrow Model"""

    id_: str = Field(default_factory=lambda: "borrow-" + uuid4().hex, alias="xt/id")
    user_id: str = Field(..., alias="borrow/user_id")
    book_id: str = Field(..., alias="borrow/book_id")
    returned: bool = Field(False, alias="borrow/returned")

    class Config:
        """Example for FastAPI"""

        extra = Extra.forbid
        schema_extra = {
            "example": {
                "borrow/user_id": "user-12345",
                "borrow/book_id": "book-12345",
            }
        }
