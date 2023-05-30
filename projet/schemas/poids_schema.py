from pydantic import BaseModel, confloat, PositiveInt


class PoidsSchema(BaseModel):
    id: PositiveInt
    valmin: confloat
    valtimbre: confloat

    class Config:
        orm_mode = True
