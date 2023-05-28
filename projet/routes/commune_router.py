from fastapi import HTTPException
from ..models import Commune
from ..controllers import commune_controller
from config.db import open_session
from .router import get_router

router = get_router()
session = open_session()


@router.get("/{commune_id}")
def get_commune(commune_id: int):
    commune = commune_controller.get_commune(session, commune_id)
    if not commune:
        raise HTTPException(status_code=404, detail="Commune not found")
    return commune


@router.post("/")
def create_commune(commune: Commune):
    return commune_controller.create_commune(session, commune)


@router.put("/{commune_id}")
def update_commune(commune_id: int, updated_commune: Commune):
    commune = commune_controller.get_commune(session, commune_id)
    if not commune:
        raise HTTPException(status_code=404, detail="Commune not found")
    return commune_controller.update_commune(session, commune, updated_commune)


@router.patch("/{commune_id}")
def update_commune(commune_id: int, updated_commune: Commune):
    commune = commune_controller.get_commune(session, commune_id)
    if not commune:
        raise HTTPException(status_code=404, detail="Commune not found")
    return commune_controller.update_commune(session, commune, updated_commune)


@router.delete("/{commune_id}")
def delete_commune(commune_id: int):
    commune = commune_controller.get_commune(session, commune_id)
    if not commune:
        raise HTTPException(status_code=404, detail="Commune not found")
    return commune_controller.delete_commune(session, commune)
