from pydantic import BaseModel
from pydantic.types import constr, PositiveInt, confloat, conint


class ConditionnementSchema(BaseModel):
    idcondit: PositiveInt
    libcondit: constr(max_length=50) = None
    poidscondit: PositiveInt
    prixcond: confloat(gt=0) = 0.0000
    ordreimp: conint(ge=0)

    class Config:
        orm_mode = True
