from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Configuration de la base de données
database_url = "mysql+pymysql://root@localhost/fromagerie"

# Déclaration de la classe de base pour les modèles
Base = declarative_base()

# Création d'une session de base de données
Session = sessionmaker()


# Fonction pour créer le moteur de base de données et lier la base et la session
def bind_engine():
    # Création du moteur de base de données
    engine = create_engine(database_url)

    # Lier la Base avec le moteur
    Base.metadata.bind = engine

    # Lier la session avec le moteur
    Session.configure(bind=engine)

