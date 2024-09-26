from fastapi import FastAPI
from routers import books, authors, genres
from database import Base, engine

# Create the database tables
Base.metadata.create_all(bind=engine)

# Initialize the FastAPI app with metadata
app = FastAPI(
    title="Bookstore Inventory API",
    description="API for managing a bookstore inventory including books, authors, and genres.",
    version="1.0.0",
)

# Include routers for different resources
app.include_router(books.router)
app.include_router(authors.router)
app.include_router(genres.router)

@app.get("/", summary="Root Endpoint")
def root():
    """
    Root endpoint to welcome users to the API.
    """
    return {"message": "Welcome to the Bookstore Inventory API!"}
