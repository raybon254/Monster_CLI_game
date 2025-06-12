from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, VARCHAR, func, DateTime
from base import Base

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer(), primary_key = True)
    name  = Column(VARCHAR())
    level  = Column(Integer())

    teams = relationship("Team" , back_populates="player" , cascade="all, delete-orphan")



