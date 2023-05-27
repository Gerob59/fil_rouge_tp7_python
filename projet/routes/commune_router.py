from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..models import Commune
from ..controllers import commune_controller
from config.sqlalchemy import bind_engine
from .router import get_router

router = get_router()


@router.get("/{commune_id}")
def get_commune(commune_id: int, db: Session = bind_engine()):
    commune = commune_controller.get_commune(db, commune_id)
    if not commune:
        raise HTTPException(status_code=404, detail="Commune not found")
    return commune


@router.post("/")
def create_commune(commune: Commune, db: Session = bind_engine()):
    return commune_controller.create_commune(db, commune)


@router.put("/{commune_id}")
def update_commune(commune_id: int, updated_commune: Commune, db: Session = bind_engine()):
    commune = commune_controller.get_commune(db, commune_id)
    if not commune:
        raise HTTPException(status_code=404, detail="Commune not found")
    return commune_controller.update_commune(db, commune, updated_commune)


@router.delete("/{commune_id}")
def delete_commune(commune_id: int, db: Session = bind_engine()):
    commune = commune_controller.get_commune(db, commune_id)
    if not commune:
        raise HTTPException(status_code=404, detail="Commune not found")
    return commune_controller.delete_commune(db, commune)
