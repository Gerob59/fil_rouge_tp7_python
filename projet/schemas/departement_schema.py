from pydantic import BaseModel


class DepartementSchema(BaseModel):
    code_dept: str  # PrimaryKey
    nom_dept: str
    ordre_aff_dept: int
