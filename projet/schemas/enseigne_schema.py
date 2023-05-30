from pydantic import BaseModel


class EnseigneSchema(BaseModel):
    id_enseigne: int  # PrimaryKey
    lb_enseigne: str
    ville_enseigne: str
    dept_enseigne: int
    class Config:
        orm_mode = True
