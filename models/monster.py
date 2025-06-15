from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, VARCHAR, func, DateTime
from models.base import Base

class Monster(Base):
    __tablename__ = "monsters"

    id = Column(Integer(), primary_key = True)
    monster  = Column(VARCHAR())
    level  = Column(Integer())
    points  = Column(Integer())
    # type monster
    # basestats
    # rarity
    # abilities

    teams = relationship("Team" , back_populates="monster")


