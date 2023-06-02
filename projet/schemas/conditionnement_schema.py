from typing import Optional
from pydantic import BaseModel
from pydantic.types import constr, confloat, conint


class ConditionnementSchema(BaseModel):
    idcondit: Optional[int]
    libcondit: constr(max_length=50) = None
    poidscondit: int
    prixcond: confloat(ge=0) = 0.0000
    ordreimp: conint(ge=0) = 0

    class Config:
        orm_mode = True
