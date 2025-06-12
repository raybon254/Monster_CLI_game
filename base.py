from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///monster.db")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

def create_table():
    Base.metadata.create_all(engine)

def drop_table():
    Base.metadata.drop_all(engine)