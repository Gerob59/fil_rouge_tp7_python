from pydantic import BaseModel


class RoleUtilisateurSchema(BaseModel):
    id: int  # PrimaryKey
    utilisateur_id: int  # ForeignKey('t_utilisateur.code_utilisateur'))
    role_id: int  # ForeignKey('t_role.codrole'))
    class Config:
        orm_mode = True