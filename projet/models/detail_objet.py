from sqlalchemy import Column, Integer, ForeignKey
from config.sqlalchemy import Base


class DetailObjet(Base):
    __tablename__ = "t_dtlcode_codobj"

    id = Column(Integer, primary_key=True)
    detail_id = Column(Integer, ForeignKey('t_dtlcode.id'))
    objet_id = Column(Integer, ForeignKey('t_objet.codobj'))
