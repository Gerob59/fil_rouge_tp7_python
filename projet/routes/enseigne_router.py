from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..models import Enseigne
from ..controllers import enseigne_controller
from config.sqlalchemy import bind_engine
from .router import get_router

router = get_router()


@router.get("/{enseigne_id}")
def get_enseigne(enseigne_id: int, db: Session = bind_engine()):
    enseigne = enseigne_controller.get_enseigne(db, enseigne_id)
    if not enseigne:
        raise HTTPException(status_code=404, detail="Enseigne not found")
    return enseigne


@router.post("/")
def create_enseigne(enseigne: Enseigne, db: Session = bind_engine()):
    return enseigne_controller.create_enseigne(db, enseigne)


@router.put("/{enseigne_id}")
def update_enseigne(enseigne_id: int, updated_enseigne: Enseigne, db: Session = bind_engine()):
    enseigne = enseigne_controller.get_enseigne(db, enseigne_id)
    if not enseigne:
        raise HTTPException(status_code=404, detail="Enseigne not found")
    return enseigne_controller.update_enseigne(db, enseigne, updated_enseigne)


@router.delete("/{enseigne_id}")
def delete_enseigne(enseigne_id: int, db: Session = bind_engine()):
    enseigne = enseigne_controller.get_enseigne(db, enseigne_id)
    if not enseigne:
        raise HTTPException(status_code=404, detail="Enseigne not found")
    return enseigne_controller.delete_enseigne(db, enseigne)
