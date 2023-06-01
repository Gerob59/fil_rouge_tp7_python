from datetime import date
from typing import Optional
from pydantic import BaseModel
from pydantic.types import constr, conint, confloat

from projet.schemas.detail_base_schema import DetailBase


class CommandeSchema(BaseModel):
    codcde: Optional[int]
    datcde: date = date.today()
    codcli: int
    timbrecli: confloat(ge=0.0) = 0.0
    timbrecde: confloat(ge=0.0) = 0.0
    nbcolis: conint(ge=1) = 1
    cheqcli: confloat(ge=0.0) = 0.0
    idcondit: conint(ge=0) = 0
    cdeComt: constr(max_length=255) = None
    barchive: conint(ge=0) = 0
    bstock: conint(ge=0) = 0
    details: list[DetailBase]

    class Config:
        orm_mode = True
