from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import Detail
from ..schemas import DetailSchema


def get_detail(db: Session, detail_id: int) -> DetailSchema:
    with db:
        detail_db = db.query(Detail).get(detail_id)
        if not detail_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Detail not found")
    return DetailSchema.from_orm(detail_db)


def get_all_details(db: Session) -> [DetailSchema]:
    with db:
        res_db = db.query(Detail).all()
        res = []
        for detail in res_db:
            res.append(DetailSchema.from_orm(detail))

    return res


def create_detail(db: Session, detail: DetailSchema) -> DetailSchema:
    with db:
        detail_db = Detail(**detail.dict())
        db.add(detail_db)
        db.commit()
        db.refresh(detail_db)
    return DetailSchema.from_orm(detail_db)


def update_detail(db: Session, detail_id: int, updated_detail: DetailSchema) -> DetailSchema:
    with db:
        detail_db = db.query(Detail).get(detail_id)
        if not detail_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Detail not found")
        updated_data = updated_detail.dict(exclude_unset=True)
        for attr, value in updated_data.items():
            setattr(detail_db, attr, value)
        db.commit()
        db.refresh(detail_db)
    return DetailSchema.from_orm(detail_db)


def delete_detail(db: Session, detail_id: int) -> dict:
    with db:
        detail_db = db.query(Detail).get(detail_id)
        if not detail_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Detail not found")
        db.delete(detail_db)
        db.commit()
    return {"message": "Detail deleted"}
