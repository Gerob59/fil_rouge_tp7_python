from projet.schemas.role_base_schema import RoleBase
from projet.schemas.utilisateur_base_schema import UtilisateurBase


class RoleSchema(RoleBase):
    users: list[UtilisateurBase]