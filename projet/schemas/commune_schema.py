from pydantic import BaseModel


class CommuneSchema(BaseModel):
    id: int  # PrimaryKey
    dep: str  # ForeignKey('t_dept.code_dept'))
    cp: str
    ville: str
