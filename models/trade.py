from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, VARCHAR, func, ForeignKey
from base import Base

class Trade(Base):
    __tablename__ = 'trades'

    id = Column(Integer, primary_key=True)
    monster_id = Column(Integer, ForeignKey('monsters.id'))
    offer_by = Column(Integer, ForeignKey('players.id'))
    requested_by = Column(Integer, ForeignKey('players.id'), nullable=True)
    status = Column(String, default='open') 

    monster = relationship('Monster')
    offer_player = relationship('Player', foreign_keys=[offer_by])
    request_player = relationship('Player', foreign_keys=[requested_by])
    trades_offered = relationship("Trade", foreign_keys='Trade.offer_by', back_populates="offer_player")
    trades_requested = relationship("Trade", foreign_keys='Trade.requested_by', back_populates="request_player")