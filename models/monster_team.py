from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, VARCHAR, func, DateTime, ForeignKey
from models.base import Base

class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer(), primary_key = True)
    player_id = Column(Integer(),ForeignKey("players.id"), nullable=False )
    monster_id = Column(Integer(),ForeignKey("monsters.id"), nullable=False )
    # level
    # experience

    player = relationship("Player" , back_populates="teams")
    monster = relationship("Monster" , back_populates="teams")

    


