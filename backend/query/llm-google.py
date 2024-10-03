import aiohttp
import re
import asyncio
import os
from dotenv import load_dotenv
load_dotenv(".env")


def Preprocess(data):

    """ Converts the data from llm into json"""
    info = data['candidates'][0]['content']['parts'][0]['text']
    # print("hi")
    info = re.sub('"', "'''", info)
    info = '{' + info + '}'
    print(info)
    info = eval(info)
    return info


async def Request(query):
    GAME = query.game
    Language = query.Language
    headers = {
        "Content-Type": "application/json"
    }
    payload = {"contents":
               [{"parts":
                 [{"text": f'''**You are a Project Guide****You are assigned the task to gamify making of Project** 
                   Make Sure that
                            - You are gentle in what you convey and also don't give all the clues for the user based on what the user what's to make.
                            - Also the Language he Pefer's will also be given.
                            - Help him by creating a Journey for him.
                   To be Taken Care of : 
                            - Each checkpoint in the Journey will allow the user make one New function which has to build based on the instruction that you give me.
                            - just tell him what the function should do ..
                            - also give him a overall perspective of the role of the function towards the Project .
                            - If the function is too difficult then only give a clue. For example you can give a hint like: You can use this specific function for this sub-task etc.
                            - Also tell him the Input and Output we expect from the function.
                    The output Format should be like the following JSON Format:
                                {{ "checkpoint_1":
                                    {{ "Instruction":
                                                "Give what has to be implemented in a interesting way like through the story.
                                                 you have to give the name of the function tobe constructed",
                                      "Overall_Vision": "What does this function contribute in entirity" ,
                                      "Input": "It should take these values as, input",
                                      "Output": "It should return these things.",
                                      "Hint": "If really tough then give Hint",
                                      "Test Cases": "Please also give three simple test cases for to check"  
                                    }},
                                    "checkpoint_2":
                                    {{ "Instruction":
                                                "Give what has to be implemented in a interesting way like through the story.
                                                 you have to give the name of the function tobe constructed",
                                      "Overall_Vision": "What does this function contribute in entirity" ,
                                      "Input": "It should take these values as, input",
                                      "Output": "It should return these things.",
                                      "Hint": "If really tough then give Hint",
                                      "Test Cases": "Please also give three simple test cases for to check"  
                                    }},
                                                ..... till we complete the project 
                                }}
                    Note: ** Give JSON OUTPUT** 
                          **ALSO DON'T GIVE ANY EXTRA TOKENS NO NEED OTHER THINGS FOLLOW THE FORMAT GIVEN**
                          ** PLEASE ENSURE YOU CLOSE ALL BRACKETS AND GIVE COMMA WHERE EVER NECESSARY BECAUSE I WILL CONVERT IT TO JSON **
                          ** GIVE TEST CASE IN PROPER WAY I WILL BE DIRECTLY USING IT TO TEST THE CODE **
                          Try to ensure that u give atleast **8 to 15 checkpoints
                   ##USER : The Project is {GAME} and the Language is {Language} '''}]}]}
    # print(query.key)
    url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={query.key}'
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload, headers=headers) as response:
            print(response.status)
            if (response.status == 200):
                data = await response.json()
                try:
                    info = Preprocess(data)
                    print(info)
                except Exception as e:
                    print(e)


class query:
    def __init__(self):
        self.game = 'Tetris'
        self.Language = 'Python'
        self.key = os.getenv('GOOGLE_API_KEY')


if __name__ == '__main__':
    Query = query()
    asyncio.run(Request(Query))
