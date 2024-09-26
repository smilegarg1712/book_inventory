from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import get_db
from typing import List

router = APIRouter(
    prefix="/books",
    tags=["books"]
)

@router.post("/", response_model=schemas.Book, summary="Create a new book", response_description="The created book")
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    """
    Create a new book.
    
    - **book**: Book information to create.
    """
    return crud.create_book(db, book)

@router.get("/", response_model=List[schemas.Book], summary="Get all books", response_description="List of all books")
def get_books(db: Session = Depends(get_db)):
    """
    Retrieve all books.
    
    Returns a list of all books in the library.
    """
    return crud.get_books(db)

@router.get("/{book_id}", response_model=schemas.Book, summary="Get a specific book", response_description="The requested book")
def get_book(book_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific book by its ID.
    
    - **book_id**: ID of the book to retrieve.
    - Returns a single book object if found, else raises a 404 error.
    """
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.put("/{book_id}", response_model=schemas.Book, summary="Update a book", response_description="The updated book")
def update_book(book_id: int, book_update: schemas.BookUpdate, db: Session = Depends(get_db)):
    """
    Update an existing book.
    
    - **book_id**: ID of the book to update.
    - **book_update**: Updated book information.
    """
    db_book = crud.get_book(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return crud.update_book(db, db_book, book_update)

@router.delete("/{book_id}", summary="Delete a book")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """
    Delete a book by its ID.
    
    - **book_id**: ID of the book to delete.
    """
    db_book = crud.get_book(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    crud.delete_book(db, db_book)
    return {"message": "Book deleted successfully"}
