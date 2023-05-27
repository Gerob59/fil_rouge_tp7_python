from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..models import ObjetCond
from ..controllers import objet_cond_controller
from config.sqlalchemy import bind_engine
from .router import get_router

router = get_router()


@router.get("/{objet_cond_id}")
def get_objet_cond(objet_cond_id: int, db: Session = bind_engine()):
    objet_cond = objet_cond_controller.get_objet_cond(db, objet_cond_id)
    if not objet_cond:
        raise HTTPException(status_code=404, detail="ObjetCond not found")
    return objet_cond


@router.post("/")
def create_objet_cond(objet_cond: ObjetCond, db: Session = bind_engine()):
    return objet_cond_controller.create_objet_cond(db, objet_cond)


@router.put("/{objet_cond_id}")
def update_objet_cond(objet_cond_id: int, updated_objet_cond: ObjetCond, db: Session = bind_engine()):
    objet_cond = objet_cond_controller.get_objet_cond(db, objet_cond_id)
    if not objet_cond:
        raise HTTPException(status_code=404, detail="ObjetCond not found")
    return objet_cond_controller.update_objet_cond(db, objet_cond, updated_objet_cond)


@router.delete("/{objet_cond_id}")
def delete_objet_cond(objet_cond_id: int, db: Session = bind_engine()):
    objet_cond = objet_cond_controller.get_objet_cond(db, objet_cond_id)
    if not objet_cond:
        raise HTTPException(status_code=404, detail="ObjetCond not found")
    return objet_cond_controller.delete_objet_cond(db, objet_cond)
