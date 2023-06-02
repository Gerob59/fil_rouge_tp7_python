from typing import Optional
from pydantic import BaseModel
from pydantic.types import constr, conint, PositiveInt

from .commune_schema import CommuneSchema
from .commande_schema import CommandeSchema


class ClientSchema(BaseModel):
    codcli: Optional[int]
    genrecli: constr(max_length=8)
    nomcli: constr(max_length=40)
    prenomcli: constr(max_length=30)
    adresse1cli: constr(max_length=50)
    adresse2cli: Optional[constr(max_length=50)]
    adresse3cli: Optional[constr(max_length=50)]
    villecli_id: CommuneSchema = {}
    telcli: constr(max_length=10)
    emailcli: constr(max_length=255)
    portcli: Optional[constr(max_length=10)]
    newsletter: conint(ge=0, le=1) = 0
    commandes: list[CommandeSchema] = []


    class Config:
        orm_mode = True
