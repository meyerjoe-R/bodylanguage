import requests
import json
import random
from example_diaries import *
import openai
from dotenv import load_dotenv
import os


def test_api():

    # Define the URL of your Flask app
    url = 'http://localhost:5000/body_language'  # Replace with your actual URL

    # Create a dictionary with the input data
    sample = random.choice(examples)

    data = {
        "prompt": sample
    }

    # Send a POST request to your Flask app
    response = requests.post(url, json=data)

    # Check the response status code and content
    if response.status_code == 200:
        result = response.json()
        print(result)
    else:
        print("Error:", response.status_code)
        print(response.text)

if __name__ == '__main__':
    test_api()