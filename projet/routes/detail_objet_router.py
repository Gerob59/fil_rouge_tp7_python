from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..models import DetailObjet
from ..controllers import detail_objet_controller
from config.sqlalchemy import bind_engine
from .router import get_router

router = get_router()


@router.get("/{detail_objet_id}")
def get_detail_objet(detail_objet_id: int, db: Session = bind_engine()):
    detail_objet = detail_objet_controller.get_detail_objet(db, detail_objet_id)
    if not detail_objet:
        raise HTTPException(status_code=404, detail="DetailObjet not found")
    return detail_objet


@router.post("/")
def create_detail_objet(detail_objet: DetailObjet, db: Session = bind_engine()):
    return detail_objet_controller.create_detail_objet(db, detail_objet)


@router.put("/{detail_objet_id}")
def update_detail_objet(detail_objet_id: int, updated_detail_objet: DetailObjet, db: Session = bind_engine()):
    detail_objet = detail_objet_controller.get_detail_objet(db, detail_objet_id)
    if not detail_objet:
        raise HTTPException(status_code=404, detail="DetailObjet not found")
    return detail_objet_controller.update_detail_objet(db, detail_objet, updated_detail_objet)


@router.delete("/{detail_objet_id}")
def delete_detail_objet(detail_objet_id: int, db: Session = bind_engine()):
    detail_objet = detail_objet_controller.get_detail_objet(db, detail_objet_id)
    if not detail_objet:
        raise HTTPException(status_code=404, detail="DetailObjet not found")
    return detail_objet_controller.delete_detail_objet(db, detail_objet)
