from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, VARCHAR, func, DateTime
from models.base import Base

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer(), primary_key = True)
    name  = Column(VARCHAR())
    nick_name  = Column(VARCHAR())
    email = Column(VARCHAR())
    gender = Column(String())
    level  = Column(Integer(), default=1)
    points = Column(Integer(), default=200)
    date = Column(DateTime , default =func.now())

    teams = relationship("Team" , back_populates="player" , cascade="all, delete-orphan")



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

    # Team relationship
    teams = relationship("Team", back_populates="player", cascade="all, delete-orphan")

    battles_as_attacker = relationship("BattleHistory",foreign_keys="[BattleHistory.attacker_id]",back_populates="attacker",cascade="all, delete-orphan")
    battles_as_defender = relationship("BattleHistory",foreign_keys="[BattleHistory.defender_id]",back_populates="defender",cascade="all, delete-orphan")
    battles_won = relationship("BattleHistory",foreign_keys="[BattleHistory.winner_id]", back_populates="winner",cascade="all, delete-orphan")