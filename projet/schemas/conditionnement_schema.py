from pydantic import BaseModel


class ConditionnementSchema(BaseModel):
    idcondit: int  # PrimaryKey
    libcondit: str
    poidscondit: int
    prixcond: float
    ordreimp: int
    # objets: List[ObjetSchema]
    class Config:
        orm_mode = True
