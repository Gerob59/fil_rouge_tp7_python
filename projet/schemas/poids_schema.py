from pydantic import BaseModel
from pydantic.types import PositiveInt, confloat


class PoidsSchema(BaseModel):
    id: PositiveInt
    valmin: confloat(gt=0)
    valtimbre: confloat(gt=0)

    class Config:
        orm_mode = True
