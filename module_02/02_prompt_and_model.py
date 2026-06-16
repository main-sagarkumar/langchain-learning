"""
PromptTemplate + Gemini
"""

import os
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# Model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

# Prompt
template = PromptTemplate.from_template(
    """
    You are a {field} mentor.

    Explain {topic} to a beginner.

    Use {example_type} examples.
    """
)

# Generate prompt
prompt = template.invoke({
    "field": "Data Science",
    "topic": "Machine Learning",
    "example_type": "cricket"
})

# Send prompt to model
response = model.invoke(prompt)

print(response.content)