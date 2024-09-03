from fastapi import Request, APIRouter, FastAPI
from fastapi.responses import JSONResponse
from fastapi.security import OA
from req import Token, CreateUser
router = FastAPI()


@router.post('/token')
async def Token_Generate(request: Request):
    print(request.username)
    print(request.password)


@router.post('/create/user')
async def Create_user(request: Request,User: CreateUser):
    print(User)