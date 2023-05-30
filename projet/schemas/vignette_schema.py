from pydantic import BaseModel
from pydantic.types import PositiveInt


class VignetteSchema(BaseModel):
    id: PositiveInt
    valmin: float = 0
    valtimbre: float = 0

    class Config:
        orm_mode = True
