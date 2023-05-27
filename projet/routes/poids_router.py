from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..models import Poids
from ..controllers import poids_controller
from config.sqlalchemy import bind_engine
from .router import get_router

router = get_router()


@router.get("/{poids_id}")
def get_poids(poids_id: int, db: Session = bind_engine()):
    poids = poids_controller.get_poids(db, poids_id)
    if not poids:
        raise HTTPException(status_code=404, detail="Poids not found")
    return poids


@router.post("/")
def create_poids(poids: Poids, db: Session = bind_engine()):
    return poids_controller.create_poids(db, poids)


@router.put("/{poids_id}")
def update_poids(poids_id: int, updated_poids: Poids, db: Session = bind_engine()):
    poids = poids_controller.get_poids(db, poids_id)
    if not poids:
        raise HTTPException(status_code=404, detail="Poids not found")
    return poids_controller.update_poids(db, poids, updated_poids)


@router.delete("/{poids_id}")
def delete_poids(poids_id: int, db: Session = bind_engine()):
    poids = poids_controller.get_poids(db, poids_id)
    if not poids:
        raise HTTPException(status_code=404, detail="Poids not found")
    return poids_controller.delete_poids(db, poids)
