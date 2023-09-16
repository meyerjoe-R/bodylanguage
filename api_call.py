import openai
from prompt import *
from dotenv import load_dotenv
import os

load_dotenv('/home/josephmeyer/git/agi_house/.env')
openai.api_key = os.getenv("OPENAI_API_KEY")

def api_completion(text, model = "gpt-3.5-turbo"):
    
    messages=[
            {
                "role": 'user',
                "content": prompt
            },
            {
                "role": "user",
                "content": "The user input is: " + text
            }
        ]

    response = openai.ChatCompletion.create(
        model=model,
        messages = messages,
        frequency_penalty=0,
        presence_penalty=0,
    )
    
    output = response.choices[0].message.content

    return output