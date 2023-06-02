from pydantic import BaseModel
from pydantic.types import constr, conint


class DepartementSchema(BaseModel):
    code_dept: constr(max_length=2) = None
    nom_dept: constr(max_length=50) = None
    ordre_aff_dept: conint(ge=0) = None

    class Config:
        orm_mode = True
