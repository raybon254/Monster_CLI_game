from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, VARCHAR, func, DateTime
from models.base import Base

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer(), primary_key=True)
    name = Column(VARCHAR())
    nick_name = Column(VARCHAR())
    email = Column(VARCHAR())
    gender = Column(String())
    level = Column(Integer(), default=1)
    points = Column(Integer(), default=200)
    experience = Column(Integer(), default=0)  
    money = Column(Integer(), default=1000)   
    date = Column(DateTime, default=func.now())

    #relationship
    from models.monster_team import Team 
    from models.monster import Monster
    from models.trade import Trade
    from models.battles import BattleHistory
    teams = relationship("Team", back_populates="player", cascade="all, delete-orphan")
    trades_offered = relationship('Trade', foreign_keys='Trade.offer_by', back_populates='offer_player')
    trades_requested = relationship('Trade', foreign_keys='Trade.requested_by', back_populates='request_player')
    battles_as_attacker = relationship("BattleHistory", back_populates="attacker", foreign_keys="[BattleHistory.attacker_id]")
    battles_as_defender = relationship('BattleHistory', foreign_keys='BattleHistory.defender_id', back_populates='defender')
    battles_won = relationship('BattleHistory', foreign_keys='BattleHistory.winner_id', back_populates='winner')
