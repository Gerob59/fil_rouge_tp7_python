from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base


class ObjetCond(Base):
    __tablename__ = "t_rel_cond"

    idrelcond = Column(Integer, primary_key=True, index=True)
    qteobjdeb = Column(Integer, default=0)
    qteobjfin = Column(Integer, default=0)
    codobj = Column(Integer, ForeignKey('t_objet.codobj'))
    codcond = Column(Integer, ForeignKey('t_conditionnement.idcondit'))
    objets = relationship("Objet", back_populates='condit')
    condit = relationship("Conditionnement", back_populates='objets')
