from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..models import Objet
from ..controllers import objet_controller
from config.sqlalchemy import bind_engine
from .router import get_router

router = get_router()


@router.get("/{objet_id}")
def get_objet(objet_id: int, db: Session = bind_engine()):
    objet = objet_controller.get_objet(db, objet_id)
    if not objet:
        raise HTTPException(status_code=404, detail="Objet not found")
    return objet


@router.post("/")
def create_objet(objet: Objet, db: Session = bind_engine()):
    return objet_controller.create_objet(db, objet)


@router.put("/{objet_id}")
def update_objet(objet_id: int, updated_objet: Objet, db: Session = bind_engine()):
    objet = objet_controller.get_objet(db, objet_id)
    if not objet:
        raise HTTPException(status_code=404, detail="Objet not found")
    return objet_controller.update_objet(db, objet, updated_objet)


@router.delete("/{objet_id}")
def delete_objet(objet_id: int, db: Session = bind_engine()):
    objet = objet_controller.get_objet(db, objet_id)
    if not objet:
        raise HTTPException(status_code=404, detail="Objet not found")
    return objet_controller.delete_objet(db, objet)
