from fastapi import FastAPI, Request, Depends
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from Auth.routes.user import router
import uuid
from comman import get_db
from req.model import Get
from utils import Answer
import json

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(router)


Excluded_paths = ['/token', '/create/user']

# @app.add_middleware('http')
# async def Middle(Request: Request, call_next):
#     if (Request.method == 'OPTIONS'):
#         await call_next()
#     if (Request.url in Excluded_paths):
#         call_next()
#     else:
#         pass


@app.post("/Task/ask")
async def Task(request: Request, data: Get,
               db=Depends(get_db)):
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
async def Getter(request_id: str, db=Depends(get_db)):
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
