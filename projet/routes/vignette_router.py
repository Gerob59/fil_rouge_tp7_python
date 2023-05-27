from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..models import Vignette
from ..controllers import vignette_controller
from config.sqlalchemy import bind_engine
from .router import get_router

router = get_router()


@router.get("/{vignette_id}")
def get_vignette(vignette_id: int, db: Session = bind_engine()):
    vignette = vignette_controller.get_vignette(db, vignette_id)
    if not vignette:
        raise HTTPException(status_code=404, detail="Vignette not found")
    return vignette


@router.post("/")
def create_vignette(vignette: Vignette, db: Session = bind_engine()):
    return vignette_controller.create_vignette(db, vignette)


@router.put("/{vignette_id}")
def update_vignette(vignette_id: int, updated_vignette: Vignette, db: Session = bind_engine()):
    vignette = vignette_controller.get_vignette(db, vignette_id)
    if not vignette:
        raise HTTPException(status_code=404, detail="Vignette not found")
    return vignette_controller.update_vignette(db, vignette, updated_vignette)


@router.delete("/{vignette_id}")
def delete_vignette(vignette_id: int, db: Session = bind_engine()):
    vignette = vignette_controller.get_vignette(db, vignette_id)
    if not vignette:
        raise HTTPException(status_code=404, detail="Vignette not found")
    return vignette_controller.delete_vignette(db, vignette)
