from fastapi import Request, APIRouter, Depends
from fastapi.responses import JSONResponse
# from fastapi.security import OA
from comman import get_db
from Auth.routes.db_utils import Check_in_db, create_user_in_db, \
    Write_token
from Auth.schema.req import USER, Login


router = APIRouter(
    prefix="",
    tags=["auth"],
    responses={401: {"user": "Not authorized"}}
)


@router.post("/token")
async def Find_user(req: Request, login: Login, db=Depends(get_db)):
    try:
        response = Check_in_db(username=login.username,
                               pwd=login.Password, db=db)
        if (response[0]):
            # print(response[1].id)
            user_obj = {"id": response[1].id,
                        "Username": response[1].username}
            token = Write_token(Information=user_obj,
                                db=db)
            if (token):
                payload = {
                    "access-token": token,
                    "access-type": "Bearer"
                }
                return JSONResponse(payload, status_code=200)
            else:
                payload = {
                    "message": "unable to create a token"
                }
                return JSONResponse(payload, status_code=500)
        else:
            payload = {
                    "message": "unable to create a token"
                }
            return JSONResponse(payload, status_code=500)
    except Exception as e:
        print("/Token", e)
        payload = {
                    "message": "unable to create a token"
                }
        return JSONResponse(payload, status_code=500)


@router.post("/create/user")
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
