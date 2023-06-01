from ..routes import client_router, commande_router, conditionnement_router
from .import_functions_from_routes import crud

# Liste des fichiers des routes
routes: [type] = [
    client_router,
    commande_router,
    conditionnement_router
]

# Ensemble de fonctions autorisées pour le rôle opérateur colis
fonctions_op_colis: set = crud(routes)

"""
L’espace gestion des colis permettra aux utilisateurs :
• La gestion des clients,
• La gestion des commandes (CRUD + calcul),
• La gestion du conditionnement (calcul final) + liste du conditionnement,
• Visualiser la liste client, et de ce fait, la fiche client,
• Visualiser les colis en cours + une historisation des mouvements des colis,
• Visualiser la liste des emballages,
• Visualiser la relation poids/colis,
• Visualiser la relation poids-vignette/colis,
• Visualiser les différentes statistiques,
    o Les statistiques s’affichent en fonction d’un intervalle de date au format mois/année,
• Le mailing client (procédure de génération du fichier texte),
• L’envoi d’emails personnalisés,
• La génération d’une impression au format papier.
"""



