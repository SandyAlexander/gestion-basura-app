from lib2to3.pytree import Base
from sqlalchemy import Column, Integer, Float, Boolean 

class Container(Base):
    __tablename__ = 'containers'
    id = Column(Integer, primary_key=True)
    level = Column(Float)
    temperature = Column(Float)
    humidity = Column(Float)
    status = Column(Boolean)  # 1 para lleno, 0 para vacío
