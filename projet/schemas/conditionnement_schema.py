from pydantic import BaseModel, constr, PositiveInt, confloat
from decimal import Decimal


class ConditionnementSchema(BaseModel):
    idcondit: PositiveInt
    libcondit: constr(max_length=50) = None
    poidscondit: PositiveInt
    prixcond: confloat = 0.0000
    ordreimp: PositiveInt

    class Config:
        orm_mode = True
