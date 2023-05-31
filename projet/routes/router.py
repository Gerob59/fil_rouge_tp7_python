from fastapi import APIRouter
from . import (
    client_router,
    commande_router,
    commune_router,
    conditionnement_router,
    departement_router,
    detail_router,
    enseigne_router,
    objet_router,
    objet_cond_router,
    poids_router,
    role_router,
    utilisateur_router,
    vignette_router,
)


def get_routes():
    router = APIRouter()
    router.include_router(client_router.router, prefix="/clients", tags=["Clients"])
    router.include_router(commande_router.router, prefix="/commandes", tags=["Commandes"])
    router.include_router(commune_router.router, prefix="/communes", tags=["Communes"])
    router.include_router(conditionnement_router.router, prefix="/conditionnements", tags=["Conditionnements"])
    router.include_router(departement_router.router, prefix="/departements", tags=["Départements"])
    router.include_router(detail_router.router, prefix="/details", tags=["Détails"])
    router.include_router(enseigne_router.router, prefix="/enseignes", tags=["Enseignes"])
    router.include_router(objet_router.router, prefix="/objets", tags=["Objets"])
    router.include_router(objet_cond_router.router, prefix="/objet_cond", tags=["Objet Cond"])
    router.include_router(poids_router.router, prefix="/poids", tags=["Poids"])
    router.include_router(role_router.router, prefix="/roles", tags=["Roles"])
    router.include_router(utilisateur_router.router, prefix="/utilisateurs", tags=["Utilisateurs"])
    router.include_router(vignette_router.router, prefix="/vignettes", tags=["Vignettes"])
    return router
