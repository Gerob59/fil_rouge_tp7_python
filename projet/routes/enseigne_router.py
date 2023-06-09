from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import enseigne_controller
from ..schemas import EnseigneSchema
from config import get_db

router = APIRouter()


@router.get("/{enseigne_id}", response_model=EnseigneSchema)
def get_enseigne(enseigne_id: int, db: Session = Depends(get_db)):
    return enseigne_controller.get_enseigne(db, enseigne_id)


@router.get("/", response_model=list[EnseigneSchema])
def get_all_enseignes(db: Session = Depends(get_db)):
    return enseigne_controller.get_all_enseignes(db)


@router.post("/", response_model=EnseigneSchema)
def create_enseigne(enseigne: EnseigneSchema, db: Session = Depends(get_db)):
    return enseigne_controller.create_enseigne(db, enseigne)


@router.put("/{enseigne_id}", response_model=EnseigneSchema)
def update_enseigne(enseigne_id: int, updated_enseigne: EnseigneSchema, db: Session = Depends(get_db)):
    return enseigne_controller.update_enseigne(db, enseigne_id, updated_enseigne)


@router.patch("/{enseigne_id}", response_model=EnseigneSchema)
def patch_enseigne(enseigne_id: int, updated_enseigne: EnseigneSchema, db: Session = Depends(get_db)):
    return enseigne_controller.update_enseigne(db, enseigne_id, updated_enseigne)


@router.delete("/{enseigne_id}", response_model=dict)
def delete_enseigne(enseigne_id: int, db: Session = Depends(get_db)):
    return enseigne_controller.delete_enseigne(db, enseigne_id)
