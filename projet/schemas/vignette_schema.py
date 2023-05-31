from pydantic import BaseModel
from pydantic.types import PositiveInt, confloat


class VignetteSchema(BaseModel):
    id: PositiveInt
    valmin: confloat(ge=0) = 0
    valtimbre: confloat(ge=0) = 0

    class Config:
        orm_mode = True
