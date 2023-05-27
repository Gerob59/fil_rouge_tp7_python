from sqlalchemy.orm import Session
from ..models import Role


def get_role(db: Session, role_id: int):
    return db.query(Role).get(role_id)


def create_role(db: Session, role: Role):
    db.add(role)
    db.commit()
    db.refresh(role)
    return role


def update_role(db: Session, role: Role, updated_role: Role):
    for attr, value in updated_role.dict().items():
        setattr(role, attr, value)
    db.commit()
    db.refresh(role)
    return role


def delete_role(db: Session, role: Role):
    db.delete(role)
    db.commit()
    return {"message": "Role deleted"}
