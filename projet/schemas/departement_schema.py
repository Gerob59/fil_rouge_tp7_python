from pydantic import BaseModel, constr, conint


class DepartementSchema(BaseModel):
    code_dept: constr(max_length=2)  # Contrainte de longueur maximale de 2 caractères
    nom_dept: constr(max_length=50)  # Contrainte de longueur maximale de 50 caractères
    ordre_aff_dept: conint(ge=0)  # Contrainte de valeur minimale de 0 pour les entiers positifs

    class Config:
        orm_mode = True
