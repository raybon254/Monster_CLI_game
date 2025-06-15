from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, VARCHAR, func, DateTime
from models.base import Base

class Monster(Base):
    __tablename__ = "monsters"

    id = Column(Integer(), primary_key = True)
    monster  = Column(VARCHAR())
    level  = Column(Integer(), default=1)
    points  = Column(Integer(), default=50)
    type_power = Column(String())

    teams = relationship("Team", back_populates="monster")
    trades = relationship("Trade", back_populates="monster")


