from pydantic import BaseModel, PositiveInt, constr


class RoleSchema(BaseModel):
    codrole: PositiveInt
    librole: constr(max_length=25) = None

    class Config:
        orm_mode = True
