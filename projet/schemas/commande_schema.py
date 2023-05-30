from datetime import datetime
from pydantic import BaseModel
from pydantic.types import constr, conint, PositiveInt, confloat


class CommandeSchema(BaseModel):
    codcde: PositiveInt
    datcde: datetime
    codcli: PositiveInt
    timbrecli: confloat(ge=0.0)
    timbrecde: confloat(ge=0.0)
    nbcolis: conint(ge=1) = 1
    cheqcli: confloat(ge=0.0)
    idcondit: conint(ge=0) = 0
    cdeComt: constr(max_length=255) = None
    barchive: conint(ge=0) = 0
    bstock: conint(ge=0) = 0

    class Config:
        orm_mode = True
