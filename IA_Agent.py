import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = os.environ.get('API_KEY')

try:
    genai.configure(api_key=API_KEY)
except Exception as e:
    raise ValueError("Failed to configure Generative AI API: " + str(e))
generation_config = {"candidate_count": 1, "temperature": 0.5}
safety_settings = {"HARASSMENT": "BLOCK_NONE", "HATE": "BLOCK_NONE", "SEXUAL": "BLOCK_NONE", "DANGEROUS": "BLOCK_NONE"}
model = genai.GenerativeModel(model_name="gemini-1.0-pro", generation_config=generation_config, safety_settings=safety_settings)

def agent_call(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        raise ValueError("Error generating content: " + str(e))

