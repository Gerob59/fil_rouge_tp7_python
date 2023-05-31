import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

KEY: str = os.getenv("key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

DRIVERNAME: str = os.getenv("DRIVERNAME", "mysql+pymysql")
HOST: str = os.getenv("HOST", "localhost")
USERNAME = os.getenv("USERNAME", "root")
PASSWORD = os.getenv("PASSWORD", "")
PORT: str = os.getenv("PORT", 3306)  # default port
DATABASE: str = os.getenv("DATABASE", "fromagerie")
DATABASE_URL = f"{DRIVERNAME}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

# Déclaration de la classe de base pour les modèles
Base = declarative_base()

# Création du moteur SQLAlchemy
engine = create_engine(DATABASE_URL)

# Création de l'objet sessionmaker
Session = sessionmaker(bind=engine)


def initialize_database() -> None:
    # Création des tables dans la base de données
    Base.metadata.create_all(engine)


def get_db() -> Session:
    """
    Le mot-clé yield est utilisé pour renvoyer temporairement db.
    Cela signifie que la première fois que la fonction est appelée, elle renverra db en tant que résultat,
    mais la fonction elle-même restera suspendue dans son état actuel.
    """
    db = Session()
    try:
        yield db
    finally:
        db.close()
