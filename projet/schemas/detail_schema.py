from typing import Optional
from pydantic import BaseModel
from pydantic.types import constr, conint


class DetailSchema(BaseModel):
    id: Optional[int]
    codcde: int
    qte: conint(ge=1) = 1
    colis: conint(ge=1) = 1
    commentaire: constr(max_length=100) = None

    class Config:
        orm_mode = True
