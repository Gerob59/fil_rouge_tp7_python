from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from ..models import Detail
from ..controllers import detail_controller
from config.db import get_db

router = APIRouter()


@router.get("/{detail_id}", response_model=Detail)
def get_detail(detail_id: int, db: Session = Depends(get_db)):
    detail = detail_controller.get_detail(db, detail_id)
    if not detail:
        raise HTTPException(status_code=404, detail="Detail not found")
    return detail


@router.get("/", response_model=list[Detail])
def get_all_details(db: Session = Depends(get_db)):
    return detail_controller.get_all_details(db)


@router.post("/", response_model=Detail)
def create_detail(detail: Detail, db: Session = Depends(get_db)):
    return detail_controller.create_detail(db, detail)


@router.put("/{detail_id}", response_model=Detail)
def update_detail(detail_id: int, updated_detail: Detail, db: Session = Depends(get_db)):
    detail = detail_controller.get_detail(db, detail_id)
    if not detail:
        raise HTTPException(status_code=404, detail="Detail not found")
    return detail_controller.update_detail(db, detail, updated_detail)


@router.patch("/{detail_id}", response_model=Detail)
def update_detail(detail_id: int, updated_detail: Detail, db: Session = Depends(get_db)):
    detail = detail_controller.get_detail(db, detail_id)
    if not detail:
        raise HTTPException(status_code=404, detail="Detail not found")
    return detail_controller.update_detail(db, detail, updated_detail)


@router.delete("/{detail_id}", response_model=dict)
def delete_detail(detail_id: int, db: Session = Depends(get_db)):
    detail = detail_controller.get_detail(db, detail_id)
    if not detail:
        raise HTTPException(status_code=404, detail="Detail not found")
    return detail_controller.delete_detail(db, detail)
