from pydantic import BaseModel


class PoidsSchema(BaseModel):
    id: int  # PrimaryKey
    valmin: float
    valtimbre: float
