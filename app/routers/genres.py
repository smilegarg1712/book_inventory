from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import get_db
from typing import List

router = APIRouter(
    prefix="/genres",
    tags=["genres"]
)

@router.post("/", response_model=schemas.Genre, summary="Create a new genre", description="Create a new genre in the database.")
def create_genre(genre: schemas.GenreCreate, db: Session = Depends(get_db)):
    return crud.create_genre(db, genre)

@router.get("/", response_model=List[schemas.Genre], summary="Get all genres", description="Retrieve a list of all genres.")
def get_genres(db: Session = Depends(get_db)):
    return crud.get_genres(db)

@router.get("/{genre_id}", response_model=schemas.Genre, summary="Get a specific genre", description="Retrieve a genre by its ID.")
def get_genre(genre_id: int, db: Session = Depends(get_db)):
    genre = crud.get_genre(db, genre_id)
    if not genre:
        raise HTTPException(status_code=404, detail="Genre not found")
    return genre

@router.put("/{genre_id}", response_model=schemas.Genre, summary="Update a genre", description="Update a genre by its ID.")
def update_genre(genre_id: int, genre_update: schemas.GenreCreate, db: Session = Depends(get_db)):
    db_genre = crud.get_genre(db, genre_id)
    if not db_genre:
        raise HTTPException(status_code=404, detail="Genre not found")
    return crud.update_genre(db, db_genre, genre_update)

@router.delete("/{genre_id}", summary="Delete a genre", description="Delete a genre by its ID.")
def delete_genre(genre_id: int, db: Session = Depends(get_db)):
    db_genre = crud.get_genre(db, genre_id)
    if not db_genre:
        raise HTTPException(status_code=404, detail="Genre not found")
    crud.delete_genre(db, db_genre)
    return {"message": "Genre deleted successfully"}
