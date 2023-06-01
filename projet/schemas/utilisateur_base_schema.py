from datetime import date
from pydantic import BaseModel
from pydantic.types import constr, PositiveInt, conint


class UtilisateurBase(BaseModel):
    code_utilisateur: PositiveInt
    nom_utilisateur: constr(max_length=50) = None
    prenom_utilisateur: constr(max_length=50) = None
    username: constr(max_length=50) = None
    password: constr(max_length=255, min_length=0)
    couleur_fond_utilisateur: conint(ge=0) = 0
    date_insc_utilisateur: date = date.today()

    class Config:
        orm_mode = True
