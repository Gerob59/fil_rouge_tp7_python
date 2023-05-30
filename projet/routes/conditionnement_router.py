from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas import ConditionnementSchema
from ..controllers import conditionnement_controller
from config.db import get_db

router = APIRouter()


@router.get("/{conditionnement_id}", response_model=ConditionnementSchema)
def get_conditionnement(conditionnement_id: int, db: Session = Depends(get_db)):
    conditionnement = conditionnement_controller.get_conditionnement(db, conditionnement_id)
    if not conditionnement:
        raise HTTPException(status_code=404, detail="Conditionnement not found")
    return conditionnement


@router.get("/", response_model=list[ConditionnementSchema])
def get_all_conditionnements(db: Session = Depends(get_db)):
    return conditionnement_controller.get_all_conditionnements(db)


@router.post("/", response_model=ConditionnementSchema)
def create_conditionnement(conditionnement: ConditionnementSchema, db: Session = Depends(get_db)):
    return conditionnement_controller.create_conditionnement(db, conditionnement)


@router.put("/{conditionnement_id}", response_model=ConditionnementSchema)
def update_conditionnement(conditionnement_id: int, updated_conditionnement: ConditionnementSchema, db: Session = Depends(get_db)):
    conditionnement = conditionnement_controller.get_conditionnement(db, conditionnement_id)
    if not conditionnement:
        raise HTTPException(status_code=404, detail="Conditionnement not found")
    return conditionnement_controller.update_conditionnement(db, conditionnement, updated_conditionnement)


@router.patch("/{conditionnement_id}", response_model=ConditionnementSchema)
def update_conditionnement(conditionnement_id: int, updated_conditionnement: ConditionnementSchema, db: Session = Depends(get_db)):
    conditionnement = conditionnement_controller.get_conditionnement(db, conditionnement_id)
    if not conditionnement:
        raise HTTPException(status_code=404, detail="Conditionnement not found")
    return conditionnement_controller.update_conditionnement(db, conditionnement, updated_conditionnement)


@router.delete("/{conditionnement_id}", response_model=dict)
def delete_conditionnement(conditionnement_id: int, db: Session = Depends(get_db)):
    conditionnement = conditionnement_controller.get_conditionnement(db, conditionnement_id)
    if not conditionnement:
        raise HTTPException(status_code=404, detail="Conditionnement not found")
    return conditionnement_controller.delete_conditionnement(db, conditionnement)
