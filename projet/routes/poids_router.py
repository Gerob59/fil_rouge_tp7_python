from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import poids_controller
from ..schemas import PoidsSchema
from config.db import get_db

router = APIRouter()


@router.get("/{poids_id}", response_model=PoidsSchema)
def get_poids(poids_id: int, db: Session = Depends(get_db)):
    return poids_controller.get_poids(db, poids_id)


@router.get("/", response_model=list[PoidsSchema])
def get_all_poids(db: Session = Depends(get_db)):
    return poids_controller.get_all_poids(db)


@router.post("/", response_model=PoidsSchema)
def create_poids(poids: PoidsSchema, db: Session = Depends(get_db)):
    return poids_controller.create_poids(db, poids)


@router.put("/{poids_id}", response_model=PoidsSchema)
def update_poids(poids_id: int, updated_poids: PoidsSchema, db: Session = Depends(get_db)):
    return poids_controller.update_poids(db, poids_id, updated_poids)


@router.patch("/{poids_id}", response_model=PoidsSchema)
def patch_poids(poids_id: int, updated_poids: PoidsSchema, db: Session = Depends(get_db)):
    return poids_controller.update_poids(db, poids_id, updated_poids)


@router.delete("/{poids_id}", response_model=dict)
def delete_poids(poids_id: int, db: Session = Depends(get_db)):
    return poids_controller.delete_poids(db, poids_id)
