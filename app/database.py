from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
load_dotenv()
USER = os.getenv("DB_USER", "default_user")  # Default value if the env variable is not set
PASSWORD = os.getenv("DB_PASSWORD", "default_password")
SQLALCHEMY_DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@localhost:5432/bookstore_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency for getting DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
