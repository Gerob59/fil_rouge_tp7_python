from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from ..models import Enseigne
from ..controllers import enseigne_controller
from config.db import get_db

router = APIRouter()


@router.get("/{enseigne_id}", response_model=Enseigne)
def get_enseigne(enseigne_id: int, db: Session = Depends(get_db)):
    enseigne = enseigne_controller.get_enseigne(db, enseigne_id)
    if not enseigne:
        raise HTTPException(status_code=404, detail="Enseigne not found")
    return enseigne


@router.get("/", response_model=list[Enseigne])
def get_all_enseignes(db: Session = Depends(get_db)):
    return enseigne_controller.get_all_enseignes(db)


@router.post("/", response_model=Enseigne)
def create_enseigne(enseigne: Enseigne, db: Session = Depends(get_db)):
    return enseigne_controller.create_enseigne(db, enseigne)


@router.put("/{enseigne_id}", response_model=Enseigne)
def update_enseigne(enseigne_id: int, updated_enseigne: Enseigne, db: Session = Depends(get_db)):
    enseigne = enseigne_controller.get_enseigne(db, enseigne_id)
    if not enseigne:
        raise HTTPException(status_code=404, detail="Enseigne not found")
    return enseigne_controller.update_enseigne(db, enseigne, updated_enseigne)


@router.patch("/{enseigne_id}", response_model=Enseigne)
def update_enseigne(enseigne_id: int, updated_enseigne: Enseigne, db: Session = Depends(get_db)):
    enseigne = enseigne_controller.get_enseigne(db, enseigne_id)
    if not enseigne:
        raise HTTPException(status_code=404, detail="Enseigne not found")
    return enseigne_controller.update_enseigne(db, enseigne, updated_enseigne)


@router.delete("/{enseigne_id}", response_model=dict)
def delete_enseigne(enseigne_id: int, db: Session = Depends(get_db)):
    enseigne = enseigne_controller.get_enseigne(db, enseigne_id)
    if not enseigne:
        raise HTTPException(status_code=404, detail="Enseigne not found")
    return enseigne_controller.delete_enseigne(db, enseigne)
