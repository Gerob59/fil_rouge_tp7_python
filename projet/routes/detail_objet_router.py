from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import detail_objet_controller
from ..schemas import DetailObjetSchema
from config.db import get_db

router = APIRouter()


@router.get("/{detail_objet_id}", response_model=DetailObjetSchema)
def get_detail_objet(detail_objet_id: int, db: Session = Depends(get_db)):
    return detail_objet_controller.get_detail_objet(db, detail_objet_id)


@router.get("/", response_model=list[DetailObjetSchema])
def get_all_detail_objets(db: Session = Depends(get_db)):
    return detail_objet_controller.get_all_detail_objets(db)


@router.post("/", response_model=DetailObjetSchema)
def create_detail_objet(detail_objet: DetailObjetSchema, db: Session = Depends(get_db)):
    return detail_objet_controller.create_detail_objet(db, detail_objet)


@router.put("/{detail_objet_id}", response_model=DetailObjetSchema)
def update_detail_objet(detail_objet_id: int, updated_detail_objet: DetailObjetSchema, db: Session = Depends(get_db)):
    return detail_objet_controller.update_detail_objet(db, detail_objet_id, updated_detail_objet)


@router.patch("/{detail_objet_id}", response_model=DetailObjetSchema)
def patch_detail_objet(detail_objet_id: int, updated_detail_objet: DetailObjetSchema, db: Session = Depends(get_db)):
    return detail_objet_controller.update_detail_objet(db, detail_objet_id, updated_detail_objet)


@router.delete("/{detail_objet_id}", response_model=dict)
def delete_detail_objet(detail_objet_id: int, db: Session = Depends(get_db)):
    return detail_objet_controller.delete_detail_objet(db, detail_objet_id)
