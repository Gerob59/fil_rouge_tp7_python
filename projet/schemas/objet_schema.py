from pydantic import BaseModel
from pydantic.types import constr, PositiveInt, confloat, conint


class ObjetSchema(BaseModel):
    codobj: PositiveInt
    libobj: constr(max_length=50) = None
    tailleobj: constr(max_length=50) = None
    puobj: confloat(gt=0) = 0.0000
    poidsobj: confloat(gt=0) = 0.0000
    indispobj: conint(ge=0) = 0
    o_imp: conint(ge=0) = 0
    o_aff: conint(ge=0) = 0
    o_cartp: conint(ge=0) = 0
    points: conint(ge=0) = 0
    o_ordre_aff: conint(ge=0) = 0

    class Config:
        orm_mode = True
