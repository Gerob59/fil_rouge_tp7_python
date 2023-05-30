from datetime import datetime
from pydantic import BaseModel


class CommandeSchema(BaseModel):
    codcde: int  # PrimaryKey
    datcde: datetime
    codcli: int  # ForeignKey('t_client.codcli'))
    timbrecli: float
    timbrecde: float
    nbcolis: int
    cheqcli: float
    idcondit: int
    cdeComt: str
    barchive: int
    bstock: int
    class Config:
        orm_mode = True
