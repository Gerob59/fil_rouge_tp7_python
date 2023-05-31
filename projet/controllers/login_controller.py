from fastapi import Depends
from sqlalchemy.orm import Session

from config import get_db
from ..models import Utilisateur


def get_user(username: str, db: Session = Depends(get_db)):
    with db:
        user = db.query(Utilisateur).filter(Utilisateur.username == username).first()
    return user