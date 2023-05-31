from projet.schemas import UtilisateurSchema
from projet.autorisation.op_colis import fonctions_op_colis


def lancer_fonction(utilisateur: UtilisateurSchema, fonction) -> None:
    role = utilisateur.role
    if role == "op_colis" and fonction in fonctions_op_colis:
        fonction()
    else:
        raise PermissionError("L'utilisateur n'a pas les autorisations nécessaires pour exécuter cette fonction.")
