from sqlalchemy import Column, String, Integer
from config import Base


class Departement(Base):
    __tablename__ = "t_dept"

    code_dept = Column(String(2), primary_key=True)
    nom_dept = Column(String(50), default=None)
    ordre_aff_dept = Column(Integer, default=0)
