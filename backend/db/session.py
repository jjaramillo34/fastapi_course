from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker

from core.config import settings
from typing import  Generator

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autoincrement=False, autoflush=False, bind=engine)

def geb_db()->Generator:
    try:
        db - SessionLocal()
        yield db
    finally:
        db.close()