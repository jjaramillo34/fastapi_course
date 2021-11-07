from sqlalchemy import create_engine, engine
from sqlalchemy import sessionmaker

from core.config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autoincrement=False, autoflush=False, bind=engine)