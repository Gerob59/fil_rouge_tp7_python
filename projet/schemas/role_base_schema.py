from typing import Optional
from pydantic import BaseModel
from pydantic.types import constr


class RoleBase(BaseModel):
    codrole: Optional[int]
    librole: constr(max_length=25) = None

    class Config:
        orm_mode = True
