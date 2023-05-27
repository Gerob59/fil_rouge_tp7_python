from sqlalchemy.orm import Session
from ..models import Detail


def get_detail(db: Session, detail_id: int):
    return db.query(Detail).get(detail_id)


def create_detail(db: Session, detail: Detail):
    db.add(detail)
    db.commit()
    db.refresh(detail)
    return detail


def update_detail(db: Session, detail: Detail, updated_detail: Detail):
    for attr, value in updated_detail.dict().items():
        setattr(detail, attr, value)
    db.commit()
    db.refresh(detail)
    return detail


def delete_detail(db: Session, detail: Detail):
    db.delete(detail)
    db.commit()
    return {"message": "Detail deleted"}
