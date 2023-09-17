from flask import Flask, request, jsonify
from api_call import *
import openai
from dotenv import load_dotenv
import os

load_dotenv('/home/josephmeyer/git/bodylanguage/.env')
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route('/body_language', methods=['POST'])

def your_api_endpoint():

    """
    expected input format: 
    {
    "prompt": "Write a summary of the impact of climate change on polar bears."
    }
    
    """

    data = request.get_json()

    if 'prompt' in data.keys():
        prompt = data.get('prompt')
    else:
        return jsonify({"error": "Invalid request data"}), 400

    # Retrieve the GPT prompt and Python code from the request
    result = api_completion(prompt)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
