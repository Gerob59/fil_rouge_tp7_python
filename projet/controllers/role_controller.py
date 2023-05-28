from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import Role


def get_role(db: Session, role_id: int):
    role = db.query(Role).get(role_id)
    if not role:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Role not found")
    return role


def get_all_roles(db: Session):
    return db.query(Role).all()


def create_role(db: Session, role: Role):
    db.add(role)
    db.commit()
    db.refresh(role)
    return role


def update_role(db: Session, role_id: int, updated_role: Role):
    role = db.query(Role).get(role_id)
    if not role:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Role not found")
    updated_data = updated_role.dict(exclude_unset=True)
    for attr, value in updated_data.items():
        setattr(role, attr, value)
    db.commit()
    db.refresh(role)
    return role


def delete_role(db: Session, role_id: int):
    role = db.query(Role).get(role_id)
    if not role:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Role not found")
    db.delete(role)
    db.commit()
    return {"message": "Role deleted"}
