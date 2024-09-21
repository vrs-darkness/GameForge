import hashlib
from sqlalchemy.orm import Session
from query.models_db import User, Data


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
        print(e)
        return False
