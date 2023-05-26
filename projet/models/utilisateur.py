from sqlalchemy import Column, Integer, String, Date
from config.sqlalchemy import Base


class Utilisateur(Base):
    __tablename__ = "t_utilisateur"

    code_utilisateur = Column(Integer, primary_key=True)
    nom_utilisateur = Column(String(50), default=None)
    prenom_utilisateur = Column(String(50), default=None)
    username = Column(String(50), default=None)
    couleur_fond_utilisateur = Column(Integer, default=0)
    date_insc_utilisateur = Column(Date)
    