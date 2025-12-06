from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from settings import get_settings
from src.utils.get_database_url import get_database_url

settings = get_settings()

engine = create_engine(
    url=settings.database_url,
    isolation_level="REPEATABLE READ"
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()