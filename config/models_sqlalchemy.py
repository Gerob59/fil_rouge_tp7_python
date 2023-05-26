from sqlalchemy import create_engine

from sqlalchemy.orm import declarative_base, sessionmaker

# Création du moteur de base de données mysql
engine = create_engine("mysql+pymysql://root@localhost/fromagerie")
Base = declarative_base()
Session = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)
