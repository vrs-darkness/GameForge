from db import Session
from uuid import uuid4
from query.models_db import Request_table
from datetime import datetime


def get_db():
    """ To Create a session for the DB to perform ORM"""
    try:
        db = Session()
        yield db

    finally:
        db.close()


def generate_uuid():
    """ To Generate unique ID for each Request"""
    return str(uuid4())


async def GET_USER_REQUEST(request, requestid):
    request_bdy = await request.body()

    return Request_table(
        request_id=requestid,
        url=request.url.path,
        method=request.method,
        ID=None,
        request=request_bdy.decode('utf-8'),
        response=None,
        status='PROCESSING',
        created_at=datetime.now())
