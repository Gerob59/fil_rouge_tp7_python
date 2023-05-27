
from fastapi import FastAPI
from . import (
    commune_router,
    client_router,
    commande_router,
    conditionnement_router,
    departement_router,
    detail_router,
    detail_objet_router,
    enseigne_router,
    objet_router,
    objet_cond_router,
    poids_router,
    role_router,
    role_utilisateur_router,
    utilisateur_router,
    vignette_router,
)

app = FastAPI()


def get_router():
    return app


def get_routes():
    app.include_router(commune_router.router, prefix="/communes", tags=["Communes"])
    app.include_router(client_router.router, prefix="/clients", tags=["Clients"])
    app.include_router(commande_router.router, prefix="/commandes", tags=["Commandes"])
    app.include_router(conditionnement_router.router, prefix="/conditionnements", tags=["Conditionnements"])
    app.include_router(departement_router.router, prefix="/departements", tags=["Départements"])
    app.include_router(detail_router.router, prefix="/details", tags=["Détails"])
    app.include_router(detail_objet_router.router, prefix="/detail_objets", tags=["Détail Objets"])
    app.include_router(enseigne_router.router, prefix="/enseignes", tags=["Enseignes"])
    app.include_router(objet_router.router, prefix="/objets", tags=["Objets"])
    app.include_router(objet_cond_router.router, prefix="/objet_cond", tags=["Objet Cond"])
    app.include_router(poids_router.router, prefix="/poids", tags=["Poids"])
    app.include_router(role_router.router, prefix="/roles", tags=["Roles"])
    app.include_router(role_utilisateur_router.router, prefix="/role_utilisateurs", tags=["Role Utilisateurs"])
    app.include_router(utilisateur_router.router, prefix="/utilisateurs", tags=["Utilisateurs"])
    app.include_router(vignette_router.router, prefix="/vignettes", tags=["Vignettes"])
