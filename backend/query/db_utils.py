import os
from dotenv import load_dotenv
import jwt
# from datetime import datetime
from sqlalchemy.orm import Session as SS
from db import Session
from query.models_db import Client, Request_table
BASE_DIR = '.env'
load_dotenv(BASE_DIR)


def Check_in_db(id: int, token: str, db: SS):
    """ Checks if the id and the token exist in db"""
    try:
        info = db.query(Client).filter(Client.ID == id)
        if (info.first()):
            info = info.filter(Client.token == token).first()
            if (info):
                return True
            else:
                return False
        else:
            return False

    except Exception as e:
        print("DB JWT CHECK: ", e)


def Check_Token(token: str):
    """To Check if the user's Token is valid or not!
        and it returns the code "VALID_000" if the token is valid
        else "EXP_000" if the token as expired
        else "INVALID_000" if the token is invalid
        in case of error "ERR_1"
    """
    try:
        session = Session()
        print("hi")
        Information = jwt.decode(token, key=os.getenv('Key'),
                                 algorithms=[os.getenv('Algo')])
        print("hi")
        print(Information)
        state = Check_in_db(Information['id'], token=token, db=session)
        if (state):
            return "VALID_000", Information['id']
        else:
            return "INVALID_000", Information['id']
    except jwt.exceptions.ExpiredSignatureError as e:
        print("JWT CHECK: ", e)
        return "EXP_000", None
    except Exception as e:
        print("JWT CHECK: ", e)
        return "ERR_1", None


def store_request(id: str, response: Request_table):
    try:
        print(f"{id} is getting created..")
        session = Session()
        session.add(response)
        session.commit()
    except Exception as e:
        print("Storing Request: ", e)


def response_save_success(id: str, response: dict, db: SS):
    try:
        info = db.query(Request_table).filter(Request_table.request_id == id)
        if (info.first()):
            info.update({Request_table.status: 'Success',
                         Request_table.response: str(response)},
                        synchronize_session=False)
            db.commit()
    except Exception as e:
        print("Issue In Storing: ", e)


def response_save_failed(id: str, response: dict, db: SS):
    try:
        info = db.query(Request_table).filter(Request_table.request_id == id)
        if (info.first()):
            info.update({Request_table.status: 'Failed',
                         Request_table.response: response},
                        synchronize_session=False)
            db.commit()
    except Exception as e:
        print("Issue In Storing: ", e)


def response_get(id: str, db: SS):
    try:
        info = db.query(Request_table).filter(
            Request_table.request_id == id).all()
        if (info[0].status == 'PROCESSING'):
            return 1, {'status': 'PROCESSING'}
        elif (info[0].status == 'Failed'):
            return 1, {"status": "Failed"}
        else:
            return 1, {"response": info[0].response}

    except Exception as e:
        print("Retrival: ", e)
        return -1, None
