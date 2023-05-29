from pydantic import BaseModel


class VignetteSchema(BaseModel):
    id: int  # PrimaryKey
    valmin: float
    valtimbre: float
