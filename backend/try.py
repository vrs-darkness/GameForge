# from openai import OpenAI
from dotenv import load_dotenv
import os
import instructor
import google.generativeai as genai
from pydantic import BaseModel

load_dotenv()

class result(BaseModel):
    data: dict


genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))


client = instructor.from_gemini(
    client=genai.GenerativeModel(
        model_name="models/gemini-1.5-flash-latest",  # model defaults to "gemini-pro"
    ),
    mode=instructor.Mode.GEMINI_JSON,
)

Game = "Tetris"
Language = "Python"
response = client.chat.completions.create(
    max_retries=100,
    messages=[{"role": "system", "content": """
        **You are a Project Guide**
        **You are assigned the task to gamify making of Project**
        Make Sure that
            - you are gentle in what you convey and also don't
                give all the clues for the user
        Based on what the user what's to make.
            - Also the Language he Pefer's will also be given.
             - Help him by creating a Journey for him.
        To be Taken Care of :
            - Each checkpoint in the Journey will allow the user make
            One New function which he has to build based on the instruction
            that you give me ..
            - just tell him what the function should do ..
            - also give him a overall perspective of the role
            of the function towards the Project .
            -  If the function is too difficult then only give a clue..
                for example : you can use this specific function
                              for this sub-task etc.
            Also tell him the Input and Output we expect from the function
        The output Format should be like the following JSON Format:
            {
                "checkpoint_1":{
                    "Instruction": "You have to Implement a Function named xyz
                                    which does....",
                    "Overall Vision": "What does this function contribute in
                                        entirity"
                    "Input": "it should take these values as input",
                    "Output": "it should return these things ...",
                    "Hint": "If really tough then give Hint",
                    "Test Cases": "Please also give three simple test cases
                                    for to check"
                }
                ..... till we complete the project
            }
        Note:
            Try to build the entire project in between 15 to 20 check points.
        """}, {"role": 'user', "content": f"""i want to make the game {Game}
               in the Language of {Language}"""}], response_model=result)

print(response)

print(type(response))

# from query.db_utils import response_save_success, response_save_failed
# from db import Session

# response_save_success("437c8ca0-b0dc-4d78-a3c3-ec7713e2fe55",
#                       {"message": "hello"}, Session())
