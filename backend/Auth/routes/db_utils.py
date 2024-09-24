import hashlib
from sqlalchemy.orm import Session
from query.models_db import User, Client
import jwt
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
load_dotenv()


def Encrypt(data: str):
    """ For Encrypting the password"""
    temp = data.encode('utf-8')
    return hashlib.sha256(temp).hexdigest()


def create_user_in_db(username: str, Name: str,
                      Password: str, mail: str,
                      db: Session):
    """ Adds new User credentials to db"""
    try:
        encrypt = Encrypt(Password)
        info = User(username=username,
                    Name=Name,
                    Password=encrypt,
                    mail=mail)
        db.add(info)
        db.commit()
        return True
    except Exception as e:
        print("Create_user", e)
        return False


def Get_from_db(user_id: int,
                db: Session):
    """ For Getting user info """
    try:
        info = db.query(User).filter(User.id == user_id).first()
        if (info):
            payload = {
                "id": info.id,
                "username": info.username
            }
            return True, payload
        else:
            payload = {"message": "User doesn't exist"}
            return False, payload
    except Exception as e:
        print(e)
        payload = {"message": "DB is Down"}
        return False, payload


def Check_in_db(username: str,
                pwd: str,
                db: Session):
    """ Checks if the user is valid"""
    try:
        encrypt = Encrypt(pwd)
        info = db.query(User).filter(User.username == username)
        info = info.filter(User.Password == encrypt)
        info = info.all()
        if not info:
            return False, 0
        else:
            return True, info[0]
    except Exception as e:
        print("DB: ", e)
        return False, -1


def Token(uid: int,
          token, db: Session):
    try:
        info = db.query(Client).filter(Client.ID == uid)
        if (info.first()):
            info.update({Client.token: token}, synchronize_session=False)
            db.commit()
        else:
            Client_info = Client(ID=uid,
                                 token=token,
                                 updated_at=datetime.now())
            db.add(Client_info)
            db.commit()
        return True
    except Exception as e:
        print("JWT-DB", e)
        return False


def Write_token(Information: dict,
                db: Session):
    """ Creating Token for the user"""
    try:
        expires = datetime.now() + timedelta(minutes=int(
            os.getenv('Time_Delay')))
        Information['expires'] = expires.strftime('%m/%d/%y %H:%M:%S')
        token = jwt.encode(Information, os.getenv('Key'), os.getenv('Algo'))
        # print(Information['id'])
        response = Token(uid=Information['id'],
                         token=token,
                         db=db)
        if (response):
            return token
        else:
            return None
    except Exception as e:
        print("JWT: ", e)
        return None
