from typing import Optional
from pydantic import BaseModel
from pydantic.types import conint


class ObjetCondSchema(BaseModel):
    idrelcond: Optional[int]
    qteobjdeb: conint(ge=0) = 0
    qteobjfin: conint(ge=0) = 0
    codobj: int
    codcond: int

    class Config:
        orm_mode = True
