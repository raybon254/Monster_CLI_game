from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, VARCHAR, func, DateTime
from base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key = True)
    name  = Column(VARCHAR())
    nick_name  = Column(VARCHAR())
    email = Column(VARCHAR())
    gender = Column(String())
    date = Column(DateTime , default =func.now())


