from sqlalchemy.orm import Session
import models, schemas


# CRUD operations for Books
def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Book).offset(skip).limit(limit).all()


def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def update_book(db: Session, db_book: models.Book, book: schemas.BookCreate):
    for var, value in vars(book).items():
        setattr(db_book, var, value) if value else None
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def delete_book(db: Session, db_book: models.Book):
    db.delete(db_book)
    db.commit()


# CRUD operations for Authors
def get_author(db: Session, author_id: int):
    return db.query(models.Author).filter(models.Author.id == author_id).first()


def get_authors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Author).offset(skip).limit(limit).all()


def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.Author(**author.dict())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def update_author(db: Session, db_author: models.Author, author: schemas.AuthorCreate):
    for var, value in vars(author).items():
        setattr(db_author, var, value) if value else None
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def delete_author(db: Session, db_author: models.Author):
    db.delete(db_author)
    db.commit()


# CRUD operations for Genres
def get_genre(db: Session, genre_id: int):
    return db.query(models.Genre).filter(models.Genre.id == genre_id).first()


def get_genres(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Genre).offset(skip).limit(limit).all()


def create_genre(db: Session, genre: schemas.GenreCreate):
    db_genre = models.Genre(**genre.dict())
    db.add(db_genre)
    db.commit()
    db.refresh(db_genre)
    return db_genre


def update_genre(db: Session, db_genre: models.Genre, genre: schemas.GenreCreate):
    for var, value in vars(genre).items():
        setattr(db_genre, var, value) if value else None
    db.add(db_genre)
    db.commit()
    db.refresh(db_genre)
    return db_genre


def delete_genre(db: Session, db_genre: models.Genre):
    db.delete(db_genre)
    db.commit()
