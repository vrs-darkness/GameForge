from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import String, Integer, JSON, Column, ForeignKey
from sqlalchemy.orm import mapped_column
load_dotenv()


class User(DeclarativeBase):
    # For each person we can have the data
    __tablename__ = 'User_data'

    id = Column(Integer, primary_key=True)
    Name = Column(String)
    Password = Column(String)
    mail = Column(String)


class Data(DeclarativeBase):
    # For Each Request we can have this table
    __tablename__ = 'User_information'

    ID = mapped_column(ForeignKey('User_data.id'))
    Request_id = Column(String, primary_key=True)
    data = Column(JSON)


connection_string = f'postgresql:{os.getenv('db_user')}//:{os.getenv('db_password')}@localhost:5432/{os.getenv('db_name')}'
Engine = create_engine(connection_string)
