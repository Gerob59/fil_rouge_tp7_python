from pydantic import BaseModel, constr, PositiveInt


class CommuneSchema(BaseModel):
    id: PositiveInt
    dep: constr(max_length=2)
    cp: constr(max_length=5) = None
    ville: constr(max_length=50) = None

    class Config:
        orm_mode = True
