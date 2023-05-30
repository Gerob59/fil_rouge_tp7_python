from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import detail_controller
from ..schemas import DetailSchema
from config.db import get_db

router = APIRouter()


@router.get("/{detail_id}", response_model=DetailSchema)
def get_detail(detail_id: int, db: Session = Depends(get_db)):
    return detail_controller.get_detail(db, detail_id)


@router.get("/", response_model=list[DetailSchema])
def get_all_details(db: Session = Depends(get_db)):
    return detail_controller.get_all_details(db)


@router.post("/", response_model=DetailSchema)
def create_detail(detail: DetailSchema, db: Session = Depends(get_db)):
    return detail_controller.create_detail(db, detail)


@router.put("/{detail_id}", response_model=DetailSchema)
def update_detail(detail_id: int, updated_detail: DetailSchema, db: Session = Depends(get_db)):
    return detail_controller.update_detail(db, detail_id, updated_detail)


@router.patch("/{detail_id}", response_model=DetailSchema)
def patch_detail(detail_id: int, updated_detail: DetailSchema, db: Session = Depends(get_db)):
    return detail_controller.update_detail(db, detail_id, updated_detail)


@router.delete("/{detail_id}", response_model=dict)
def delete_detail(detail_id: int, db: Session = Depends(get_db)):
    return detail_controller.delete_detail(db, detail_id)
