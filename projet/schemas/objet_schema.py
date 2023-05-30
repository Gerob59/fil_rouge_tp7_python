from pydantic import BaseModel


class ObjetSchema(BaseModel):
    codobj: int  # PrimaryKey
    libobj: str
    tailleobj: str
    puobj: float
    poidsobj: float
    indispobj: int
    o_imp: int
    o_aff: int
    o_cartp: int
    points: int
    o_ordre_aff: int
    # condit: List[ObjetCondSchema]  # relationship("ObjetCond", back_populates='objets')
    class Config:
        orm_mode = True
