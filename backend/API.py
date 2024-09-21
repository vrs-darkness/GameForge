from fastapi import FastAPI, Request, Depends
from fastapi.responses import JSONResponse
from req.model import Get, USER
import uuid
from comman import get_db
from utils import Answer
from query.db_utils import create_user_in_db
import json

app = FastAPI()


# @app.add_middleware('http')
# async def Middle(Request: Request, call_next):
#     if (Request.method == 'OPTIONS'):
#         await call_next()
# #     pass


@app.post("/create/user")
async def Create_user(req: Request, Request: USER, db=Depends(get_db)):
    try:
        response = create_user_in_db(username=Request.username,
                                     Name=Request.Name,
                                     Password=Request.Password,
                                     mail=Request.mail,
                                     db=db)
        if (response):
            payload = {'message': "Successfully Created!!"}
            return JSONResponse(payload, status_code=200)
        else:
            payload = {'message': "Some Issues Encountered!!"}
            return JSONResponse(payload, status_code=500)
    except Exception as e:
        print(e)
        payload = {'message': "Some Issues Encountered!!"}
        return JSONResponse(payload, status_code=500)


@app.post("/Task/ask")
async def Task(request: Request, data: Get):
    """
    This API gamifies the Project to be made
    and gives back the steps as an output to
    the user
    """
    try:
        uuid_new = uuid.uuid4()
        Language = data.Language
        Game = data.Game
        Payload = {
            "id": uuid_new,
            "payload": {"Language": Language, "Game": Game}
        }
        _ = Answer.delay(json.dumps(Payload, default=str))
        response = {
            "id": uuid_new,
            "status": "Processing"
        }
        response = json.dumps(response, default=str)
        return JSONResponse(response, status_code=202)
    except Exception as e:
        print(e)
        response = {
            "id": uuid_new,
            "status": "Failed"
        }
        return JSONResponse(response, status_code=500)


@app.get("/Task/get/{id}")
async def Getter(request_id: str):
    """
        This helps to retrive
        the data from the backend
    """
    try:
        print(request_id)
        response = {
            "id": request_id,
            "payload": None,
            "status": "Success"
        }
        return JSONResponse(response, status_code=200)
    except Exception as e:
        print(e)
        response = {
            "id": request_id,
            "payload": None,
            "status": "Success"
        }
        return JSONResponse(response, status_code=500)
