from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..models import Detail
from ..controllers import detail_controller
from config.sqlalchemy import bind_engine
from .router import get_router

router = get_router()


@router.get("/{detail_id}")
def get_detail(detail_id: int, db: Session = bind_engine()):
    detail = detail_controller.get_detail(db, detail_id)
    if not detail:
        raise HTTPException(status_code=404, detail="Detail not found")
    return detail


@router.post("/")
def create_detail(detail: Detail, db: Session = bind_engine()):
    return detail_controller.create_detail(db, detail)


@router.put("/{detail_id}")
def update_detail(detail_id: int, updated_detail: Detail, db: Session = bind_engine()):
    detail = detail_controller.get_detail(db, detail_id)
    if not detail:
        raise HTTPException(status_code=404, detail="Detail not found")
    return detail_controller.update_detail(db, detail, updated_detail)


@router.delete("/{detail_id}")
def delete_detail(detail_id: int, db: Session = bind_engine()):
    detail = detail_controller.get_detail(db, detail_id)
    if not detail:
        raise HTTPException(status_code=404, detail="Detail not found")
    return detail_controller.delete_detail(db, detail)
