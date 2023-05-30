from datetime import datetime
from pydantic import BaseModel


class UtilisateurSchema(BaseModel):
    code_utilisateur: int  # PrimaryKey
    nom_utilisateur: str
    prenom_utilisateur: str
    username: str
    couleur_fond_utilisateur: int
    date_insc_utilisateur: datetime
    class Config:
        orm_mode = True