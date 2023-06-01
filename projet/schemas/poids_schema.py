from typing import Optional

from pydantic import BaseModel
from pydantic.types import confloat


class PoidsSchema(BaseModel):
    id: Optional[int]
    valmin: confloat(ge=0.0)
    valtimbre: confloat(ge=0.0)

    class Config:
        orm_mode = True
