from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from req.model import Get
from openai import AzureOpenAI
from dotenv import load_dotenv
import os
import json
load_dotenv()

app = FastAPI()


@app.post("/Task/ask")
async def Task(request: Request, data: Get):
    """
    This API gamifies the Project to be made
    and gives back the steps as an output to
    the user
    """
    try:
        Language = data.Language
        Game = data.Game
        client = AzureOpenAI(api_key=os.getenv('AZURE_OPENAI_API_KEY'),
                            api_version=os.getenv('AZURE_API_VERSION'),
                            azure_endpoint=os.getenv('AZURE_API_URL'))
        response = client.chat.completions.create(
            model=os.getenv('AZURE_DEPLOYMENT_NAME'),
            messages=[{"role": "system", "content": """
                    **You are a Project Guide**
                    **You are assigned the task to gamify making of Project**
                    Make Sure that
                            - You are gentle in what you convey and also don't
                            give all the clues for the user based on what the
                            user what's to make.
                            - Also the Language he Pefer's will also be given.
                            - Help him by creating a Journey for him.
                    To be Taken Care of :
                            - Each checkpoint in the Journey will allow the user
                            make one New function which he has to build based
                            on the instruction that you give me ..
                            - just tell him what the function should do ..
                            - also give him a overall perspective of the role
                            of the function towards the Project .
                            -  If the function is too difficult then only give a
                                clue.
                                For example you can give a hint like: You can use
                                                    this specific function for
                                                    this sub-task etc.
                            - Also tell him the Input and Output we expect from
                            the function
                        The output Format should be like the following JSON Format:
                            {
                                "checkpoint_1":{
                                    "Instruction": "You have to Implement a
                                                    Function named xyz which does",
                                    "Overall Vision": "What does this function
                                                    contribute in entirity"
                                    "Input": "It should take these values as
                                            input",
                                    "Output": "It should return these things.",
                                    "Hint": "If really tough then give Hint",
                                    "Test Cases": "Please also give three simple
                                                test cases for to check"}
                                ..... till we complete the project
                            }
                        Note:
                            Try to build the entire project in between 15 to 20
                                    check-points."""}, {"role": 'user',
                                                        "content": f"""i want to
                                                            make the game {Game}
                                                            in the Language of
                                                            {Language}"""}], temperature=1, response_format={'type': "json_object"})
        response = response.choices[0].message.content
        if (isinstance(response, str)):
            Passed = "failed"
        else:
            Passed = "Passed"
        result = {
            "result":  response,
            "catagory": Passed
        }
        return JSONResponse(result, status_code=200)
    except Exception as e:
        print(e)
        result = {
            "result": "Err"
        }

