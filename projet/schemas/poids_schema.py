from pydantic import BaseModel


class PoidsSchema(BaseModel):
    id: int  # PrimaryKey
    valmin: float
    valtimbre: float
    class Config:
        orm_mode = True