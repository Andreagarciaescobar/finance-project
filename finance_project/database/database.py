
import os 

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

def get_db_name():
    return os.environ.get('DB_NAME', 'StockDatabase')

def get_db_password():
    return os.environ.get('DB_PASSWORD', 'develop')

def get_db_host():
    return f"{os.environ.get('DB_HOST', 'localhost')}:\
    {os.environ.get('DB_PORT', 5432)}"

def get_db_user():
    return os.environ.get('DB_USER', 'postgres')

def get_db_url():
    return f"postgresql://{get_db_user()}:{get_db_password()}@{get_db_host()}/{get_db_name()}"


engine = create_engine(
    create_db_url()
)

SessionLocal = sessionmaker(autocommit=False, autoflush = False, bind=engine)

Base = declarative_base()
