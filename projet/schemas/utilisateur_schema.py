from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from pydantic.types import constr, PositiveInt, conint


class UtilisateurSchema(BaseModel):
    code_utilisateur: PositiveInt
    nom_utilisateur: constr(max_length=50) = None
    prenom_utilisateur: constr(max_length=50) = None
    username: constr(max_length=50) = None
    couleur_fond_utilisateur: conint(ge=0) = 0
    date_insc_utilisateur: Optional[datetime]

    class Config:
        orm_mode = True
