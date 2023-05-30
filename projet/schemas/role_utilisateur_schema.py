from pydantic import BaseModel, PositiveInt


class RoleUtilisateurSchema(BaseModel):
    id: PositiveInt
    utilisateur_id: PositiveInt
    role_id: PositiveInt

    class Config:
        orm_mode = True
