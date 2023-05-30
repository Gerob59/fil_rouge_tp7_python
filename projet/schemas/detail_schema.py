from pydantic import BaseModel, constr, conint, PositiveInt


class DetailSchema(BaseModel):
    id: PositiveInt
    codcde: PositiveInt
    qte: conint(ge=1) = 1
    colis: conint(ge=1) = 1
    commentaire: constr(max_length=100) = None

    class Config:
        orm_mode = True
