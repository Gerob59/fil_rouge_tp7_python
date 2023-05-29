from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import Detail
from ..schemas import DetailSchema


def get_detail(db: Session, detail_id: int):
    detail = db.query(Detail).get(detail_id)
    if not detail:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Detail not found")
    return detail


def get_all_details(db: Session):
    return db.query(Detail).all()


def create_detail(db: Session, detail: DetailSchema):
    db.add(detail)
    db.commit()
    db.refresh(detail)
    return detail


def update_detail(db: Session, detail_id: int, updated_detail: DetailSchema):
    detail = db.query(Detail).get(detail_id)
    if not detail:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Detail not found")
    updated_data = updated_detail.dict(exclude_unset=True)
    for attr, value in updated_data.items():
        setattr(detail, attr, value)
    db.commit()
    db.refresh(detail)
    return detail


def delete_detail(db: Session, detail_id: int):
    detail = db.query(Detail).get(detail_id)
    if not detail:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Detail not found")
    db.delete(detail)
    db.commit()
    return {"message": "Detail deleted"}
