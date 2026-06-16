import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="""
You are an expert Data Science mentor.

Explain Machine Learning to a 12-year-old student
using a cricket example.
"""
)

print(response.text)