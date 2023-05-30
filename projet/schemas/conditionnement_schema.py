from pydantic import BaseModel
from pydantic.types import constr, PositiveInt, confloat


class ConditionnementSchema(BaseModel):
    idcondit: PositiveInt
    libcondit: constr(max_length=50) = None
    poidscondit: PositiveInt
    prixcond: confloat(gt=0) = 0.0000
    ordreimp: PositiveInt

    class Config:
        orm_mode = True
