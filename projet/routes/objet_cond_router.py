from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from ..models import ObjetCond
from ..controllers import objet_cond_controller
from config.db import get_db

router = APIRouter()


@router.get("/{objet_cond_id}", response_model=ObjetCond)
def get_objet_cond(objet_cond_id: int, db: Session = Depends(get_db)):
    objet_cond = objet_cond_controller.get_objet_cond(db, objet_cond_id)
    if not objet_cond:
        raise HTTPException(status_code=404, detail="ObjetCond not found")
    return objet_cond


@router.get("/", response_model=list[ObjetCond])
def get_all_objet_cond(db: Session = Depends(get_db)):
    return objet_cond_controller.get_all_objet_cond(db)


@router.post("/", response_model=ObjetCond)
def create_objet_cond(objet_cond: ObjetCond, db: Session = Depends(get_db)):
    return objet_cond_controller.create_objet_cond(db, objet_cond)


@router.put("/{objet_cond_id}", response_model=ObjetCond)
def update_objet_cond(objet_cond_id: int, updated_objet_cond: ObjetCond, db: Session = Depends(get_db)):
    objet_cond = objet_cond_controller.get_objet_cond(db, objet_cond_id)
    if not objet_cond:
        raise HTTPException(status_code=404, detail="ObjetCond not found")
    return objet_cond_controller.update_objet_cond(db, objet_cond, updated_objet_cond)


@router.patch("/{objet_cond_id}", response_model=ObjetCond)
def update_objet_cond(objet_cond_id: int, updated_objet_cond: ObjetCond, db: Session = Depends(get_db)):
    objet_cond = objet_cond_controller.get_objet_cond(db, objet_cond_id)
    if not objet_cond:
        raise HTTPException(status_code=404, detail="ObjetCond not found")
    return objet_cond_controller.update_objet_cond(db, objet_cond, updated_objet_cond)


@router.delete("/{objet_cond_id}", response_model=dict)
def delete_objet_cond(objet_cond_id: int, db: Session = Depends(get_db)):
    objet_cond = objet_cond_controller.get_objet_cond(db, objet_cond_id)
    if not objet_cond:
        raise HTTPException(status_code=404, detail="ObjetCond not found")
    return objet_cond_controller.delete_objet_cond(db, objet_cond)
