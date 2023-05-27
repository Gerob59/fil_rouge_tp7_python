from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..models import Conditionnement
from ..controllers import conditionnement_controller
from config.sqlalchemy import bind_engine
from .router import get_router

router = get_router()


@router.get("/{conditionnement_id}")
def get_conditionnement(conditionnement_id: int, db: Session = bind_engine()):
    conditionnement = conditionnement_controller.get_conditionnement(db, conditionnement_id)
    if not conditionnement:
        raise HTTPException(status_code=404, detail="Conditionnement not found")
    return conditionnement


@router.post("/")
def create_conditionnement(conditionnement: Conditionnement, db: Session = bind_engine()):
    return conditionnement_controller.create_conditionnement(db, conditionnement)


@router.put("/{conditionnement_id}")
def update_conditionnement(conditionnement_id: int, updated_conditionnement: Conditionnement, db: Session = bind_engine()):
    conditionnement = conditionnement_controller.get_conditionnement(db, conditionnement_id)
    if not conditionnement:
        raise HTTPException(status_code=404, detail="Conditionnement not found")
    return conditionnement_controller.update_conditionnement(db, conditionnement, updated_conditionnement)


@router.delete("/{conditionnement_id}")
def delete_conditionnement(conditionnement_id: int, db: Session = bind_engine()):
    conditionnement = conditionnement_controller.get_conditionnement(db, conditionnement_id)
    if not conditionnement:
        raise HTTPException(status_code=404, detail="Conditionnement not found")
    return conditionnement_controller.delete_conditionnement(db, conditionnement)
