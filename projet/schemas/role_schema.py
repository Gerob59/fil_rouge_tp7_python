from .role_base_schema import RoleBase
from .utilisateur_base_schema import UtilisateurBase


class RoleSchema(RoleBase):
    users: list[UtilisateurBase]
