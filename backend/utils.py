import os
from openai import AzureOpenAI
from dotenv import load_dotenv
from db import Session
from query.db_utils import response_save_success, response_save_failed
from celery import Celery
# import asyncio
import json
load_dotenv()
celery = Celery("worker", broker='redis://localhost:6379/0',
                backend='redis://localhost:6379/0')


@celery.task
def Answer(Payload: dict):
    print(Payload)
    try:
        client = AzureOpenAI(api_key=os.getenv('AZURE_OPENAI_API_KEY'),
                             api_version=os.getenv('AZURE_API_VERSION'),
                             azure_endpoint=os.getenv('AZURE_API_URL'))
        Payload = json.loads(Payload)
        Game = Payload['payload']['Game']
        Language = Payload['payload']['Language']
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
                            - Each checkpoint in the Journey will allow the
                                user make one New function which he has to
                                build based on the instruction that you give
                                me.
                            - just tell him what the function should do ..
                            - also give him a overall perspective of the role
                            of the function towards the Project .
                            -  If the function is too difficult then only give
                                a clue.
                                For example you can give a hint like: You can
                                                    use this specific function
                                                    for this sub-task etc.
                            - Also tell him the Input and Output we expect from
                            the function
                        The output Format should be like the following JSON
                            Format:
                            {
                                "checkpoint_1":{
                                    "Instruction": "Give what has to be
                                                    implemented in a
                                                    interesting way like
                                                    through the story.
                                                    you have to give the name
                                                    of the function to
                                                    be constructed",
                                    "Overall Vision": "What does this function
                                                    contribute in entirity"
                                    "Input": "It should take these values as
                                            input",
                                    "Output": "It should return these things.",
                                    "Hint": "If really tough then give Hint",
                                    "Test Cases": "Please also give three
                                                    simple test cases for to
                                                    check"}
                                ..... till we complete the project
                            }
                        Note:
                            Try to ensure that u give atleast **8 to 15
                            checkpoints**"""},
                      {"role": 'user', "content": f"""i want to
                                                make the game {Game}
                                                in the Language of
                                                {Language}"""}],
            temperature=1, response_format={'type': "json_object"})
        results = response.choices[0].message.content
        response_save_success(Payload["id"], results, db=Session())
        print("Done..")
    except Exception as e:
        payload = {
            "Message": f"Error Occured {e}"
        }
        response_save_failed(Payload["id"], payload, db=Session())
