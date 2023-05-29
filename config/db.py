from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Configuration de la base de données MySQL
DATABASE = {
    'drivername': 'mysql+pymysql',
    'host': 'localhost',  # par défaut
    'port': '3306',  # par défaut
    'username': 'root',
    'password': '',
    'database': 'fromagerie',
}

# Création de l'URL de connexion à la base de données
DB_URL = f"{DATABASE['drivername']}://{DATABASE['username']}:{DATABASE['password']}@{DATABASE['host']}:{DATABASE['port']}/{DATABASE['database']}"
# DB_URL = "mysql+pymysql://root@localhost/fromagerie"

# Déclaration de la classe de base pour les modèles
Base = declarative_base()

# Création du moteur SQLAlchemy
engine = create_engine(DB_URL)

# Création de l'objet sessionmaker
Session = sessionmaker(bind=engine)


def initialize_database() -> None:
    # Création des tables dans la base de données
    Base.metadata.create_all(engine)


def get_db() -> Session:
    db = Session()
    try:
        yield db
    finally:
        db.close()
