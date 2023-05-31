from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from pydantic.types import constr, PositiveInt


class UtilisateurBase(BaseModel):
    code_utilisateur: PositiveInt
    nom_utilisateur: constr(max_length=50) = None
    prenom_utilisateur: constr(max_length=50) = None
    username: constr(max_length=50) = None
    password: constr(max_length=255)
    couleur_fond_utilisateur: int = 0
    date_insc_utilisateur: Optional[datetime]

    class Config:
        orm_mode = True
