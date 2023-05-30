from pydantic import BaseModel, PositiveInt


class VignetteSchema(BaseModel):
    id: PositiveInt
    valmin: float = 0
    valtimbre: float = 0

    class Config:
        orm_mode = True
