import requests
import json

# Define the URL of your Flask app
url = 'http://localhost:5000/body_language'  # Replace with your actual URL

# Create a dictionary with the input data
data = {
    "prompt": "I drank four beers and slept for four hours."
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
