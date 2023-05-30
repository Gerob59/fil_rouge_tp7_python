from pydantic import BaseModel, PositiveInt


class DetailObjetSchema(BaseModel):
    id: PositiveInt
    detail_id: PositiveInt
    objet_id: PositiveInt

    class Config:
        orm_mode = True
