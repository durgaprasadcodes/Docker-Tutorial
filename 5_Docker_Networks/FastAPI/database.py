from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

database_url = "postgresql+psycopg2://postgres:admin@pgsql_container:5432/dockerdb"

engine = create_engine(database_url)

SessionLocal = sessionmaker(autoflush=False,autocommit=False,bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()