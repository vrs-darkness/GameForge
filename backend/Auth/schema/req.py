from pydantic import BaseModel


class USER(BaseModel):
    username: str
    Name: str
    Password: str
    mail: str


class Login(BaseModel):
    username: str
    Password: str
