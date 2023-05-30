from pydantic import BaseModel
from pydantic.types import constr, PositiveInt


class RoleSchema(BaseModel):
    codrole: PositiveInt
    librole: constr(max_length=25) = None

    class Config:
        orm_mode = True
