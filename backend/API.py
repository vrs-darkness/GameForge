from fastapi import FastAPI, Request, Depends
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from Auth.routes.user import router
from comman import get_db, generate_uuid, GET_USER_REQUEST
from query.db_utils import store_request, Check_Token, response_get
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


Excluded_paths = ['/token', '/create/user', '/docs', '/openapi.json']


@app.middleware('http')
async def Middle(Request: Request, call_next):
    if (Request.method == "OPTIONS"):
        response = await call_next(Request)
        return response
    uuid_request = generate_uuid()
    Request.state.uuid = uuid_request
    request_obj = await GET_USER_REQUEST(Request, uuid_request)
    if (Request.url.path not in Excluded_paths):
        # print(Request.url)
        if ("Authorization" not in Request.headers):
            response = {
                "message": "Authorization header Missing!!",
                "status_code": 401
            }
            request_obj.response = str(response)
            store_request(uuid_request, request_obj)
            return JSONResponse(response, 401)
        elif ("Bearer" not in Request.headers['Authorization']):
            response = {
                "message": "Bearer Token not Found",
                "status_code": 401
            }
            request_obj.response = str(response)
            store_request(uuid_request, request_obj)
            return JSONResponse(response, 401)
        else:
            # print(Request.headers['Authorization'][7:])
            response, id = Check_Token(Request.headers['Authorization'][7:])
            # print(response)
            # print(id)
            request_obj.ID = id
            Request.state.id = id
    else:
        Request.state.id = None
    # print(Request.url.path)
    response = await call_next(Request)

    if Request.url.path in ['/docs', '/openapi.json']:
        return response
    request_obj.response = str(Request.state.response)
    store_request(uuid_request, request_obj)
    return response


@app.post("/Task/ask")
async def Task(request: Request, data: Get,
               db=Depends(get_db)):
    """
    This API gamifies the Project to be made
    and gives back the steps as an output to
    the user
    """
    try:
        uuid_new = request.state.uuid
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
        request.state.response = response
        response = json.dumps(response, default=str)
        return JSONResponse(response, status_code=202)
    except Exception as e:
        print(e)
        response = {
            "id": uuid_new,
            "status": "Failed"
        }
        request.state.response = response
        return JSONResponse(response, status_code=500)


@app.get("/Task/get/{id}")
async def Getter(request: Request, request_id: str, db=Depends(get_db)):
    """
        This helps to retrive
        the data from the backend
    """
    try:
        # print(request_id)
        pos, payload = response_get(request_id, db)
        if (pos == 1):
            response = {
                "id": request_id,
                "payload": payload,
                "status": "Success"
            }
            request.state.response = response
            return JSONResponse(response, status_code=200)
        else:
            response = {
                "id": request_id,
                "payload": "Unable to fetch"
            }
            request.state.response = response
            return JSONResponse(response, status_code=100)
    except Exception as e:
        print(e)
        response = {
            "id": request_id,
            "Message": "Unable to fetch right Now!!"
        }
        request.state.response = response
        return JSONResponse(response, status_code=500)
