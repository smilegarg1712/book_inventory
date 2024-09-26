from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import get_db
from typing import List


# Create a router for authors
router = APIRouter(
    prefix="/authors",
    tags=["authors"]
)

# Create Author
@router.post("/", response_model=schemas.Author, summary="Create a new author")
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    """Create a new author."""
    return crud.create_author(db, author)

# Get All Authors
@router.get("/", response_model=List[schemas.Author], summary="Retrieve a list of authors")
def get_authors(db: Session = Depends(get_db)):
    """Retrieve a list of authors with pagination."""
    return crud.get_authors(db)

# Get Author by ID
@router.get("/{author_id}", response_model=schemas.Author, summary="Get an author by ID")
def get_author(author_id: int, db: Session = Depends(get_db)):
    """Retrieve a specific author by their ID."""
    author = crud.get_author(db, author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author

# Update Author
@router.put("/{author_id}", response_model=schemas.Author, summary="Update an existing author")
def update_author(author_id: int, author_update: schemas.AuthorCreate, db: Session = Depends(get_db)):
    """Update an existing author by their ID."""
    db_author = crud.get_author(db, author_id)
    if not db_author:
        raise HTTPException(status_code=404, detail="Author not found")
    return crud.update_author(db, db_author, author_update)

# Delete Author
@router.delete("/{author_id}", summary="Delete an author by ID")
def delete_author(author_id: int, db: Session = Depends(get_db)):
    """Delete a specific author by their ID."""
    db_author = crud.get_author(db, author_id)
    if not db_author:
        raise HTTPException(status_code=404, detail="Author not found")
    crud.delete_author(db, db_author)
    return {"message": "Author deleted successfully"}

