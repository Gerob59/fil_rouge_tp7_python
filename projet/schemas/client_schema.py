from pydantic import BaseModel


class ClientSchema(BaseModel):
    codcli: int  # PrimaryKey
    genrecli: str
    nomcl: str
    prenomcli: str
    adresse1cli: str
    adresse2cli: str
    adresse3cli: str
    villecli_id: int  # ForeignKey('t_communes.id')
    telcli: str
    emailcli: str
    portcli: str
    newsletter: int
