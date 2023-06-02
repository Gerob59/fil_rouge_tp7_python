from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import Detail
from ..schemas import DetailSchema


def get_detail(db: Session, detail_id: int) -> DetailSchema:
    '''
        retourne un detail en fonction d'un id donné
        :param db: Session
        :param detail_id: int
        :return: DetailSchema
        '''
    with db:
        detail_db = db.query(Detail).get(detail_id)
        if not detail_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Detail not found")
    return DetailSchema.from_orm(detail_db)


def get_all_details(db: Session) -> [DetailSchema]:
    '''
        retourne tous les detail de la bdd
        :param db: Session
        :return: [DetailSchema]
        '''
    with db:
        resultat = db.query(Detail).all()
    return resultat


def create_detail(db: Session, detail: DetailSchema) -> DetailSchema:
    '''
        ajoute un nouveau detail en bdd
        :param db: Session
        :param detail: DetailSchema
        :return: DetailSchema
        '''
    with db:
        detail_db = Detail(**detail.dict())
        db.add(detail_db)
        db.commit()
        db.refresh(detail_db)
    return DetailSchema.from_orm(detail_db)


def update_detail(db: Session, detail_id: int, updated_detail: DetailSchema) -> DetailSchema:
    '''
       modifie un detail en bdd
       :param db: Session
       :param detail_id: int
       :param updated_detail: DetailSchema
       :return: DetailSchema
       '''
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
    '''
        supprime un detail en bdd
        :param db: Session
        :param detail_id: int
        :return: dict
        '''
    with db:
        detail_db = db.query(Detail).get(detail_id)
        if not detail_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Detail not found")
        db.delete(detail_db)
        db.commit()
    return {"message": "Detail deleted"}
