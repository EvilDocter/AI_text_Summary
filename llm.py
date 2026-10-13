import os
import json
from dotenv import load_dotenv
from google import genai

# Load the API key from the .env file
load_dotenv()

# Connect to Gemini using our API key
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Choose the Gemini model
MODEL = "gemini-3.5-flash-lite"

# Send a prompt to Gemini and return its answer
def ask_ai(prompt):
    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )
    return response.text

# Ask Gemini for a JSON response
def ask_ai_json(prompt):
    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config={
            "response_mime_type": "application/json"
        }
    )
    # Convert the JSON text into a Python dictionary
    return json.loads(response.text)