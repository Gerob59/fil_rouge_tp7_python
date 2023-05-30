from pydantic import BaseModel, constr, EmailStr, conint, PositiveInt


class ClientSchema(BaseModel):
    codcli: PositiveInt
    genrecli: constr(max_length=8)
    nomcli: constr(max_length=40)
    prenomcli: constr(max_length=30)
    adresse1cli: constr(max_length=50)
    adresse2cli: constr(max_length=50)
    adresse3cli: constr(max_length=50)
    villecli_id: PositiveInt
    telcli: constr(max_length=10)
    emailcli: EmailStr
    portcli: constr(max_length=10)
    newsletter: conint(ge=0, le=1) = 0

    class Config:
        orm_mode = True
