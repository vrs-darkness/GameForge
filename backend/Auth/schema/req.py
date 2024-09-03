from pydantic import BaseModel


class Token(BaseModel):

    username: str
    password: str


class CreateUser(BaseModel):
    Name: str
    username: str
    password: str
    subscriped: str
