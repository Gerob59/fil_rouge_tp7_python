from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from ..models import DetailObjet
from ..controllers import detail_objet_controller
from config.db import get_db

router = APIRouter()


@router.get("/{detail_objet_id}", response_model=DetailObjet)
def get_detail_objet(detail_objet_id: int, db: Session = Depends(get_db)):
    detail_objet = detail_objet_controller.get_detail_objet(db, detail_objet_id)
    if not detail_objet:
        raise HTTPException(status_code=404, detail="DetailObjet not found")
    return detail_objet


@router.get("/", response_model=list[DetailObjet])
def get_all_detail_objets(db: Session = Depends(get_db)):
    return detail_objet_controller.get_all_detail_objets(db)


@router.post("/", response_model=DetailObjet)
def create_detail_objet(detail_objet: DetailObjet, db: Session = Depends(get_db)):
    return detail_objet_controller.create_detail_objet(db, detail_objet)


@router.put("/{detail_objet_id}", response_model=DetailObjet)
def update_detail_objet(detail_objet_id: int, updated_detail_objet: DetailObjet, db: Session = Depends(get_db)):
    detail_objet = detail_objet_controller.get_detail_objet(db, detail_objet_id)
    if not detail_objet:
        raise HTTPException(status_code=404, detail="DetailObjet not found")
    return detail_objet_controller.update_detail_objet(db, detail_objet, updated_detail_objet)


@router.patch("/{detail_objet_id}", response_model=DetailObjet)
def update_detail_objet(detail_objet_id: int, updated_detail_objet: DetailObjet, db: Session = Depends(get_db)):
    detail_objet = detail_objet_controller.get_detail_objet(db, detail_objet_id)
    if not detail_objet:
        raise HTTPException(status_code=404, detail="DetailObjet not found")
    return detail_objet_controller.update_detail_objet(db, detail_objet, updated_detail_objet)


@router.delete("/{detail_objet_id}", response_model=dict)
def delete_detail_objet(detail_objet_id: int, db: Session = Depends(get_db)):
    detail_objet = detail_objet_controller.get_detail_objet(db, detail_objet_id)
    if not detail_objet:
        raise HTTPException(status_code=404, detail="DetailObjet not found")
    return detail_objet_controller.delete_detail_objet(db, detail_objet)
