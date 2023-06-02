from typing import Optional
from pydantic import BaseModel
from pydantic.types import constr, conint


class EnseigneSchema(BaseModel):
    id_enseigne: Optional[int]
    lb_enseigne: constr(max_length=50) = None
    ville_enseigne: constr(max_length=50) = None
    dept_enseigne: conint(ge=0) = 0

    class Config:
        orm_mode = True
