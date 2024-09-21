from sqlalchemy.orm import declarative_base
from sqlalchemy import String, Integer, JSON, Column, ForeignKey
from sqlalchemy.orm import mapped_column

Base = declarative_base()


class User(Base):
    # For each person we can have the data
    __tablename__ = 'User_data'

    id = Column(Integer, primary_key=True)
    Name = Column(String)
    username = Column(String, unique=True)
    Password = Column(String)
    mail = Column(String, unique=True)


class Data(Base):
    # For Each Request we can have this table
    __tablename__ = 'User_information'

    ID = mapped_column(ForeignKey('User_data.id'))
    Request_id = Column(String, primary_key=True)
    request = Column(JSON)
    response_Status = Column(Integer)
    response = Column(JSON)
