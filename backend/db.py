from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from query.models_db import Base

from sqlalchemy.orm import sessionmaker
load_dotenv()

connection_string = f'postgresql+psycopg2://{os.getenv('db_user')}:{os.getenv('db_password')}@localhost:5432/{os.getenv('db_name')}'
# print(connection_string)
Engine = create_engine(connection_string)

try:
    Base.metadata.create_all(Engine)
    print("Started Engine...")
except Exception as e:
    print(e)


Session = sessionmaker(autocommit=False, bind=Engine)
