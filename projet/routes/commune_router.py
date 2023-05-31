from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import commune_controller
from ..schemas import CommuneSchema
from config import get_db

router = APIRouter()


@router.get("/{commune_id}", response_model=CommuneSchema)
def get_commune(commune_id: int, db: Session = Depends(get_db)):
    return commune_controller.get_commune(db, commune_id)


@router.get("/", response_model=list[CommuneSchema])
def get_all_communes(db: Session = Depends(get_db)):
    return commune_controller.get_all_communes(db)


@router.post("/", response_model=CommuneSchema)
def create_commune(commune: CommuneSchema, db: Session = Depends(get_db)):
    return commune_controller.create_commune(db, commune)


@router.put("/{commune_id}", response_model=CommuneSchema)
def update_commune(commune_id: int, updated_commune: CommuneSchema, db: Session = Depends(get_db)):
    return commune_controller.update_commune(db, commune_id, updated_commune)


@router.patch("/{commune_id}", response_model=CommuneSchema)
def patch_commune(commune_id: int, updated_commune: CommuneSchema, db: Session = Depends(get_db)):
    return commune_controller.update_commune(db, commune_id, updated_commune)


@router.delete("/{commune_id}", response_model=dict)
def delete_commune(commune_id: int, db: Session = Depends(get_db)):
    return commune_controller.delete_commune(db, commune_id)
