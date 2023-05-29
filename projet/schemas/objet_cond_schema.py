from typing import List
from pydantic import BaseModel


class ObjetCondSchema(BaseModel):
    idrelcond: int  # PrimaryKey
    qteobjdeb: int
    qteobjfin: int
    codobj: int  # ForeignKey('t_objet.codobj')
    codcond: int  # ForeignKey('t_conditionnement.idcondit')
    # objets: List[ObjetSchema]  # relationship("Objet", back_populates='condit')
    # condit: List[ConditionnementSchema]  # relationship("Conditionnement", back_populates='objets')
