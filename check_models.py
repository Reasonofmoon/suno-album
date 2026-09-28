import os

import google.generativeai as genai
from dotenv import load_dotenv

# The key is read from the environment, never from source. See .env.example.
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise SystemExit("GEMINI_API_KEY not found. Create a .env file with GEMINI_API_KEY=your_key_here")

genai.configure(api_key=API_KEY)

print("Available Models:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"- {m.name}")
