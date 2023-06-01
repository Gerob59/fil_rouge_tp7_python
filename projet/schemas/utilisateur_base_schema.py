from datetime import date
from typing import Optional

from pydantic import BaseModel
from pydantic.types import constr, conint


class UtilisateurBase(BaseModel):
    code_utilisateur: Optional[int] = None
    nom_utilisateur: constr(max_length=50) = None
    prenom_utilisateur: constr(max_length=50) = None
    username: constr(max_length=50) = None
    password: constr(min_length=0, max_length=255)
    couleur_fond_utilisateur: conint(ge=0) = 0
    date_insc_utilisateur: date = date.today()

    class Config:
        orm_mode = True
