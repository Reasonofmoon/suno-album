import google.generativeai as genai
import os

API_KEY = "AIzaSyC7zXTr2IsmwCEPC3lej1Uh2hQmF-hEfDs"
genai.configure(api_key=API_KEY)

print("Available Models:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"- {m.name}")
