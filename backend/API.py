from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from req.model import Get
import uuid
from utils import Answer
import json

app = FastAPI()


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
