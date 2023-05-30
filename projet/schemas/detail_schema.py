from pydantic import BaseModel


class DetailSchema(BaseModel):
    id: int  # PrimaryKey
    codcde: int  # ForeignKey('t_entcde.codcde'), index=True
    qte: int
    colis: int
    commentaire: str
    class Config:
        orm_mode = True
