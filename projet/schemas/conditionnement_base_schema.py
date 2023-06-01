from typing import Optional

from pydantic import BaseModel
from pydantic.types import constr, PositiveInt, confloat, conint

from projet.schemas import CommandeSchema


class ConditionnementBase(BaseModel):
    idcondit: Optional[int]
    libcondit: constr(max_length=50) = None
    poidscondit: int
    prixcond: confloat(ge=0) = 0.0000
    ordreimp: conint(ge=0) = 0
    commandes: list[CommandeSchema]

    class Config:
        orm_mode = True
