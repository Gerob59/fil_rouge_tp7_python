from pydantic import BaseModel, PositiveInt, confloat, constr


class ObjetSchema(BaseModel):
    codobj: PositiveInt
    libobj: constr(max_length=50) = None
    tailleobj: constr(max_length=50) = None
    puobj: confloat = 0.0000
    poidsobj: confloat = 0.0000
    indispobj: PositiveInt = 0
    o_imp: PositiveInt = 0
    o_aff: PositiveInt = 0
    o_cartp: PositiveInt = 0
    points: PositiveInt = 0
    o_ordre_aff: PositiveInt = 0

    class Config:
        orm_mode = True
