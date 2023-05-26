from sqlalchemy import create_engine

from sqlalchemy.orm import declarative_base, sessionmaker

from projet.models import *

# Création du moteur de base de données mysql
#Base.metadata.create_all(engine)

Base = declarative_base()
Session = sessionmaker()

def bind_engine():
    engine = create_engine("mysql+pymysql://root@localhost/fromagerie")
    Base.metadata.bind = engine
    Session.configure(bind=engine)