from fastapi import HTTPException
from ..models import Poids
from ..controllers import poids_controller
from config.db import open_session
from .router import get_router

router = get_router()
session = open_session()


@router.get("/{poids_id}")
def get_poids(poids_id: int):
    poids = poids_controller.get_poids(session, poids_id)
    if not poids:
        raise HTTPException(status_code=404, detail="Poids not found")
    return poids


@router.post("/")
def create_poids(poids: Poids):
    return poids_controller.create_poids(session, poids)


@router.put("/{poids_id}")
def update_poids(poids_id: int, updated_poids: Poids):
    poids = poids_controller.get_poids(session, poids_id)
    if not poids:
        raise HTTPException(status_code=404, detail="Poids not found")
    return poids_controller.update_poids(session, poids, updated_poids)


@router.patch("/{poids_id}")
def update_poids(poids_id: int, updated_poids: Poids):
    poids = poids_controller.get_poids(session, poids_id)
    if not poids:
        raise HTTPException(status_code=404, detail="Poids not found")
    return poids_controller.update_poids(session, poids, updated_poids)


@router.delete("/{poids_id}")
def delete_poids(poids_id: int):
    poids = poids_controller.get_poids(session, poids_id)
    if not poids:
        raise HTTPException(status_code=404, detail="Poids not found")
    return poids_controller.delete_poids(session, poids)
