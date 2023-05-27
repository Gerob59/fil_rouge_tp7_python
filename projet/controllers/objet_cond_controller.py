from sqlalchemy.orm import Session
from ..models import ObjetCond


def get_objet_cond(db: Session, objet_cond_id: int):
    return db.query(ObjetCond).get(objet_cond_id)


def create_objet_cond(db: Session, objet_cond: ObjetCond):
    db.add(objet_cond)
    db.commit()
    db.refresh(objet_cond)
    return objet_cond


def update_objet_cond(db: Session, objet_cond: ObjetCond, updated_objet_cond: ObjetCond):
    for attr, value in updated_objet_cond.dict().items():
        setattr(objet_cond, attr, value)
    db.commit()
    db.refresh(objet_cond)
    return objet_cond


def delete_objet_cond(db: Session, objet_cond: ObjetCond):
    db.delete(objet_cond)
    db.commit()
    return {"message": "ObjetCond deleted"}
