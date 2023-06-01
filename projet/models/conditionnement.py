from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import relationship

from config import Base


class Conditionnement(Base):
    __tablename__ = "t_conditionnement"

    idcondit = Column(Integer, primary_key=True)
    libcondit = Column(String(50), default=None)
    poidscondit = Column(Integer)
    prixcond = Column(Numeric, default=0.0000)
    ordreimp = Column(Integer)

    details = relationship("Detail", secondary="t_dtlcode_idcondit", back_populates="conditionnements")
