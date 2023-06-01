from sqlalchemy import Column, Integer, ForeignKey
from config.db import Base


class DetailConditionnement(Base):
    __tablename__ = "t_dtlcode_idcondit"

    id = Column(Integer, primary_key=True)
    detail_id = Column(Integer, ForeignKey('t_dtlcode.id'))
    conditionnement_id = Column(Integer, ForeignKey('t_conditionnement.idcondit'))
