from pydantic import BaseModel
from pydantic.types import PositiveInt, conint


class ObjetCondSchema(BaseModel):
    idrelcond: PositiveInt
    qteobjdeb: conint(ge=0) = 0
    qteobjfin: conint(ge=0) = 0
    codobj: PositiveInt
    codcond: PositiveInt

    class Config:
        orm_mode = True
