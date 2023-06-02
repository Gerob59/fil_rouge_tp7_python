from projet.schemas import UtilisateurSchema
from projet.autorisation.op_colis import fonctions_op_colis


def lancer_fonction(utilisateur: UtilisateurSchema, fonction) -> None:
    '''
    cette fonction permet de verifier si un utilisateur donné a le droit d'utilisé une fonction donnée, et la lance s'il le peut
    :param utilisateur: UtilisateurSchema
    :param fonction: function
    :return: None
    '''
    roles = utilisateur.roles

    if "op_colis" in roles and fonction in fonctions_op_colis:
        fonction()
    else:
        raise PermissionError("L'utilisateur n'a pas les autorisations nécessaires pour exécuter cette fonction.")

