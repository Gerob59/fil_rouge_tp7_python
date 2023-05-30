from pydantic import BaseModel, constr, conint, PositiveInt


class EnseigneSchema(BaseModel):
    id_enseigne: PositiveInt
    lb_enseigne: constr(max_length=50) = None
    ville_enseigne: constr(max_length=50) = None
    dept_enseigne: conint(ge=0) = 0

    class Config:
        orm_mode = True
