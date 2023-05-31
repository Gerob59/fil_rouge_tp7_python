from .role_base_schema import RoleBase
from .utilisateur_base_schema import UtilisateurBase


class UtilisateurSchema(UtilisateurBase):
    roles: list[RoleBase]
