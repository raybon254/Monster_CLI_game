from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from .base import Base

class BattleHistory(Base):
    __tablename__ = 'battle_history'

    id = Column(Integer, primary_key=True)
    attacker_id = Column(Integer, ForeignKey("players.id"))
    defender_id = Column(Integer, ForeignKey("players.id"))
    winner_id = Column(Integer, ForeignKey("players.id"))
    timestamp = Column(DateTime, default=func.now())

    attacker = relationship('Player', foreign_keys=[attacker_id], back_populates='battles_as_attacker')
    defender = relationship('Player', foreign_keys=[defender_id], back_populates='battles_as_defender')
    winner = relationship('Player', foreign_keys=[winner_id], back_populates='battles_won')
