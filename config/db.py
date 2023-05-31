from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .setting import settings

if settings.database_password:
    SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
else:
    SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://{settings.database_username}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db() -> Session:
    db = Session()
    try:
        yield db
    finally:
        db.close()
