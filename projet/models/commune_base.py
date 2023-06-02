from sqlalchemy import Column, String, Integer, Index

from config import Base


class CommuneBase(Base):
    __tablename__ = "t_communes"

    id = Column(Integer, primary_key=True)
    cp = Column(String(5), default=None)
    ville = Column(String(50), default=None)