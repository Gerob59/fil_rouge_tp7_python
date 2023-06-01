from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import conditionnement_controller
from ..schemas import ConditionnementSchema
from config import get_db

router = APIRouter()


@router.get("/{conditionnement_id}", response_model=ConditionnementSchema)
def get_conditionnement(conditionnement_id: int, db: Session = Depends(get_db)):
    return conditionnement_controller.get_conditionnement(db, conditionnement_id)


@router.get("/", response_model=list[ConditionnementSchema])
def get_all_conditionnements(db: Session = Depends(get_db)):
    return conditionnement_controller.get_all_conditionnements(db)


@router.post("/", response_model=ConditionnementSchema)
def create_conditionnement(conditionnement: ConditionnementSchema, db: Session = Depends(get_db)):
    return conditionnement_controller.create_conditionnement(db, conditionnement)


@router.put("/{conditionnement_id}", response_model=ConditionnementSchema)
def update_conditionnement(conditionnement_id: int, updated_conditionnement: ConditionnementSchema, db: Session = Depends(get_db)):
    return conditionnement_controller.update_conditionnement(db, conditionnement_id, updated_conditionnement)


@router.patch("/{conditionnement_id}", response_model=ConditionnementSchema)
def patch_conditionnement(conditionnement_id: int, updated_conditionnement: ConditionnementSchema, db: Session = Depends(get_db)):
    return conditionnement_controller.update_conditionnement(db, conditionnement_id, updated_conditionnement)


@router.delete("/{conditionnement_id}", response_model=dict)
def delete_conditionnement(conditionnement_id: int, db: Session = Depends(get_db)):
    return conditionnement_controller.delete_conditionnement(db, conditionnement_id)
