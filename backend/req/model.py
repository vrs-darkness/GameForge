from pydantic import BaseModel, Field


class Get(BaseModel):

    Language: str = Field(
        description='The Language you want to use for the Step Making')
    Game: str = Field(
        description='The Game that user wants to convert into steps')


class USER(BaseModel):
    username: str
    Name: str
    Password: str
    mail: str
