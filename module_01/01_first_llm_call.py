"""
First Gemini API Call

Purpose:
    Understand the minimum code needed to interact with an LLM.
"""

# ==================================================
# Imports
# ==================================================

import os
from dotenv import load_dotenv
from google import genai

# ==================================================
# Load Environment Variables
# ==================================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

# ==================================================
# Create Client
# ==================================================

client = genai.Client(api_key=api_key)

# ==================================================
# Call Model
# ==================================================

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain LangChain to a beginner in 5 bullet points."
)

# ==================================================
# Print Response
# ==================================================

print(response.text)