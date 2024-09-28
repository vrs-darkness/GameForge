from sqlalchemy.orm import declarative_base
from sqlalchemy import String, Integer, Column, ForeignKey, DateTime, Text
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


class Client(Base):
    # Storing JWT Token for each person
    __tablename__ = 'Client_data'

    ID = mapped_column(ForeignKey('User_data.id'), primary_key=True)
    token = Column(String)
    updated_at = Column(DateTime)


class Request_table(Base):
    # For Storing result of each request
    __tablename__ = 'Request_data'

    request_id = Column(String, primary_key=True)
    url = Column(String)
    method = Column(String)
    ID = mapped_column(ForeignKey('User_data.id'), nullable=True)
    request = Column(Text)
    response = Column(Text)
    status = Column(String)
    created_at = Column(DateTime)
