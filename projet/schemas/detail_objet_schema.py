from pydantic import BaseModel


class DetailObjetSchema(BaseModel):
    id: int  # PrimaryKey
    detail_id: int  # ForeignKey('t_dtlcode.id')
    objet_id: int  # ForeignKey('t_objet.codobj')
    class Config:
        orm_mode = True
