from pydantic import BaseModel
from pydantic.types import PositiveInt


class ObjetCondSchema(BaseModel):
    idrelcond: PositiveInt
    qteobjdeb: PositiveInt = 0
    qteobjfin: PositiveInt = 0
    codobj: PositiveInt
    codcond: PositiveInt

    class Config:
        orm_mode = True
