from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class AuthorBase(BaseModel):
    name: str
    biography: str

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int
    books: List["Book"] = []

    class Config:
        orm_mode = True

class GenreBase(BaseModel):
    name: str

class GenreCreate(GenreBase):
    pass

class Genre(GenreBase):
    id: int
    books: List["Book"] = []

    class Config:
        orm_mode = True

class BookBase(BaseModel):
    title: str
    publication_date: date
    price: float

class BookCreate(BookBase):
    author_id: int
    genre_id: int

class BookUpdate(BookBase):
    author_id: Optional[int] = None
    genre_id: Optional[int] = None

class Book(BookBase):
    id: int
    author: Author
    genre: Genre

    class Config:
        orm_mode = True
